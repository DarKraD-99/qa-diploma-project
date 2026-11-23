import uuid
import requests
import allure


base_url = "https://api.github.com"
token = "ВВЕСТИ_СВОЙ_ТОКЕН"


@allure.title("Авторизация в GitHub")
@allure.description(
    "Тест проверяет авторизацию пользователя в GitHub"
)
@allure.feature("GitHub")
@allure.severity(allure.severity_level.CRITICAL)
def test_positive_auth() -> None:
    """
    Тест проверяет авторизацию пользователя в GitHub
    :return: None
    """
    url = base_url

    headers = {
        "Authorization": f"Bearer {token}"
    }

    with allure.step("Передача запроса на авторизацию"):
        resp = requests.get(url + "/user", headers=headers)

    with allure.step("Проверка статус-кода"):
        assert resp.status_code == 200


@allure.title("Создание репозитория")
@allure.description(
    "Тест проверяет создание репозитория"
)
@allure.feature("GitHub")
@allure.severity(allure.severity_level.NORMAL)
def test_positive_create_repo() -> None:
    """
    Тест проверяет создание репозитория в GitHub
    :return: None
    """
    url = base_url
    repo_name = "test_repo" + str(uuid.uuid4())[:8]

    project = {
        "name": repo_name,
        "description": "Описание репозитория",
        "private": False,
        "has_issues": True,
        "has_projects": True,
        "has_wiki": True
    }

    headers = {
        "Authorization": f"Bearer {token}"
    }

    with allure.step("Запрос на получение имени пользователя"):
        user_resp = requests.get(url + "/user", headers=headers)
        username = user_resp.json()["login"]

    with allure.step("Передача запроса на создание репозитория"):
        resp = requests.post(
            url + "/user/repos", json=project, headers=headers
        )

    with allure.step("Проверка статус-кода"):
        assert resp.status_code == 201

    with allure.step("Удаление текущего репозитория"):
        delete_resp = requests.delete(
            url + f"/repos/{username}/{repo_name}", headers=headers
        )

    with allure.step("Проверка статус-кода"):
        assert delete_resp.status_code == 204


@allure.title("Редактирование описания репозитория")
@allure.description(
    "Тест проверяет изменение описания репозитория"
)
@allure.feature("GitHub")
@allure.severity(allure.severity_level.NORMAL)
def test_positive_change_desc() -> None:
    """
    Тест проверяет изменение описания репозитория в GitHub
    :return: None
    """
    url = base_url
    repo_name = "test_repo" + str(uuid.uuid4())[:8]

    project = {
        "name": repo_name,
        "description": "Описание репозитория",
        "private": False,
        "has_issues": True,
        "has_projects": True,
        "has_wiki": True
    }

    new_desc = {
        "description": "Новое описание репозитория",
    }

    headers = {
        "Authorization": f"Bearer {token}"
    }

    with allure.step("Запрос на получение имени пользователя"):
        user_resp = requests.get(url + "/user", headers=headers)
        username = user_resp.json()["login"]

    with allure.step("Передача запроса на создание репозитория"):
        create_repo = requests.post(
            url + "/user/repos", json=project, headers=headers
        )

    with allure.step("Проверка статус-кода"):
        assert create_repo.status_code == 201

    try:
        with allure.step(
            "Передача запроса на обновление описания репозитория"
        ):
            resp = requests.patch(
                url + f"/repos/{username}/{repo_name}", json=new_desc,
                headers=headers
            )

        with allure.step("Передача запроса на проверку обновлённого описания"):
            get_repo = requests.get(
                url + f"/repos/{username}/{repo_name}",
                headers=headers
            )

        with allure.step("Проверки статус-кода"):
            assert resp.status_code == 200
            assert get_repo.status_code == 200

        with allure.step("Проверка нового описания репозитория"):
            assert (
                get_repo.json()["description"] == "Новое описание репозитория"
            )

    finally:
        with allure.step("Передача запроса на удаление репозитория"):
            delete_resp = requests.delete(
                url + f"/repos/{username}/{repo_name}", headers=headers
                )

        with allure.step("Проверка статус-кода"):
            assert delete_resp.status_code == 204


@allure.title("Удаление репозитория")
@allure.description(
    "Тест проверяет удаление репозитория"
)
@allure.feature("GitHub")
@allure.severity(allure.severity_level.NORMAL)
def test_positive_delete_repo() -> None:
    """
    Тест проверяет удаление репозитория пользователя в GitHub
    :return: None
    """
    url = base_url
    repo_name = "test_repo" + str(uuid.uuid4())[:8]

    project = {
        "name": repo_name,
        "description": "Описание репозитория",
        "private": False,
        "has_issues": True,
        "has_projects": True,
        "has_wiki": True
    }

    headers = {
        "Authorization": f"Bearer {token}"
    }

    with allure.step("Запрос на получение имени пользователя"):
        user_resp = requests.get(url + "/user", headers=headers)
        username = user_resp.json()["login"]

    with allure.step("Передача запроса на создание репозитория"):
        create_repo = requests.post(
            url + "/user/repos", json=project, headers=headers
        )

    with allure.step("Проверка статус-кода"):
        assert create_repo.status_code == 201

    with allure.step("Передача запроса на удаление репозитория"):
        resp = requests.delete(
            url + f"/repos/{username}/{repo_name}", headers=headers
        )

    with allure.step("Проверка статус-кода"):
        assert resp.status_code == 204


@allure.title("Авторизация в GitHub без токена")
@allure.description(
    "Тест проверяет авторизацию пользователя в GitHub "
    "без токена пользователя"
)
@allure.feature("GitHub")
@allure.severity(allure.severity_level.MINOR)
def test_negative_auth() -> None:
    """
    Тест проверяет авторизацию пользователя в GitHub
    без токена пользователя
    :return: None
    """
    url = base_url
    token = ""

    headers = {
        "Authorization": f"Bearer {token}"
    }

    with allure.step("Передача запроса на авторизацию"):
        resp = requests.get(url + "/user", headers=headers)

    with allure.step("Проверка статус-кода"):
        assert resp.status_code == 401


@allure.title("Удаление несуществующего репозитория")
@allure.description(
    "Тест проверяет удаление несуществующего репозитория"
)
@allure.feature("GitHub")
@allure.severity(allure.severity_level.NORMAL)
def test_negative_delete_repo() -> None:
    """
    Тест проверяет удаление несуществующего репозитория в GitHub
    :return: None
    """
    url = base_url
    repo_name = "test_repo" + str(uuid.uuid4())[:8]

    headers = {
        "Authorization": f"Bearer {token}"
    }

    with allure.step("Запрос на получение имени пользователя"):
        user_resp = requests.get(url + "/user", headers=headers)
        username = user_resp.json()["login"]

    with allure.step("Передача запроса на удаление репозитория"):
        resp = requests.delete(
            url + f"/repos/{username}/{repo_name}", headers=headers
        )
    with allure.step("Проверка статус-кода"):
        assert resp.status_code == 404
