import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.PageAuth import PageAuth
from pages.PageRepo import PageRepo


@pytest.fixture()
def driver():
    """
    Фикстура для инициализации и завершения работы драйвера,
    а также для создания рабочей среды для авторизации
    """
    options = webdriver.ChromeOptions()
    options.add_argument(r"--user-data-dir=C:\selenium_profile")

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


@allure.title("Авторизация в GitHub")
@allure.description(
    "Тест проверяет авторизацию пользователя в GitHub"
)
@allure.feature("GitHub")
@allure.severity(allure.severity_level.CRITICAL)
def test_github_auth(driver: webdriver.Chrome) -> None:
    """
    Тест проверяет авторизацию пользователя в GitHub
    :param driver: WebDriver - объект драйвера, переданный фикстурой
    :return: None
    """
    wait = WebDriverWait(driver, 10)
    page_auth = PageAuth(driver)

    with allure.step("Открытие главной страницы GitHub"):
        page_auth.open_gh()

    avatars = driver.find_elements(
        By.CSS_SELECTOR, "img[alt='User avatar']"
    )

    if not avatars:
        with allure.step("Нажатие на кнопку перехода к авторизации"):
            page_auth.sign_in_button()

        with allure.step("Ввод логина"):
            page_auth.input_login()

        with allure.step("Ввод пароля"):
            page_auth.input_password()

        with allure.step("Клик по кнопке авторизации"):
            page_auth.click_auth_btn()

    user_avatar = wait.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "img[alt='User avatar']")
    ))
    with allure.step("Проверка наличия аватара после авторизации"):
        assert user_avatar.is_displayed()


@allure.title("Создание репозитория")
@allure.description(
    "Тест проверяет создание репозитория"
)
@allure.feature("GitHub")
@allure.severity(allure.severity_level.NORMAL)
def test_create_repo(driver: webdriver.Chrome) -> None:
    """
    Тест проверяет создание репозитория в GitHub
    :param driver: WebDriver - объект драйвера, переданный фикстурой
    :return: None
    """
    page_open_gh = PageAuth(driver)

    with allure.step("Открытие главной страницы GitHub"):
        page_open_gh.open_gh()

    page_create_repo = PageRepo(driver)
    with allure.step("Нажатие на кнопку создания"):
        page_create_repo.btn_create()

    with allure.step("Кнопка перехода к созданию репозитория"):
        page_create_repo.btn_new_repo()

    with allure.step("Ввод имени репозитория"):
        page_create_repo.input_name_repo("Diploma_project")

    with allure.step("Ввод описания репозитория"):
        page_create_repo.input_desc_repo("Описание репозитория")

    with allure.step("Нажатие на кнопку создания репозитория"):
        page_create_repo.btn_create_repo()

    with allure.step("Проверка имени репозитория после его создания"):
        assert page_create_repo.actual_name() == "Diploma_project"

    page_delete_repo = PageRepo(driver)

    with allure.step("Кнопка перехода в настройки репозитория"):
        page_delete_repo.btn_settings()

    with allure.step("Кнопка удаления репозитория"):
        page_delete_repo.btn_delete()

    with allure.step("Кнопка подтверждения удаления"):
        page_delete_repo.btn_delete_access()

    with allure.step("Кнопка подтверждения о прочтении последствий удаления"):
        page_delete_repo.btn_read_access()

    with allure.step("Поле ввода владельца и названия"):
        page_delete_repo.delete_repo_confirm()

    with allure.step("Удаление"):
        page_delete_repo.btn_delete_confirm()

    with allure.step("Проверка наличия сообщения об успешном удалении"):
        assert "Diploma_project" in page_delete_repo.alert_message()


@allure.title("Редактирование описания репозитория")
@allure.description(
    "Тест проверяет изменение описания репозитория"
)
@allure.feature("GitHub")
@allure.severity(allure.severity_level.NORMAL)
def test_update_descr_repo(driver: webdriver.Chrome) -> None:
    """
    Тест проверяет изменение описания репозитория в GitHub
    :param driver: WebDriver - объект драйвера, переданный фикстурой
    :return: None
    """
    page_open_gh = PageAuth(driver)

    with allure.step("Открытие главной страницы GitHub"):
        page_open_gh.open_gh()

    page_create_repo = PageRepo(driver)

    with allure.step("Нажатие на кнопку создания"):
        page_create_repo.btn_create()

    with allure.step("Кнопка перехода к созданию репозитория"):
        page_create_repo.btn_new_repo()

    with allure.step("Ввод имени репозитория"):
        page_create_repo.input_name_repo("Diploma_project_test")

    with allure.step("Ввод описания репозитория"):
        page_create_repo.input_desc_repo("Описание репозитория")

    with allure.step("Кнопка создания файла README в репозитории"):
        page_create_repo.btn_readme()

    with allure.step("Нажатие на кнопку создания репозитория"):
        page_create_repo.btn_create_repo()

    page_change_descr = PageRepo(driver)

    with allure.step("Кнопка, открывающая раздел 'About' внутри репозитория"):
        page_change_descr.btn_edit()

    with allure.step("Поле ввода описания"):
        page_change_descr.input_descr()

    with allure.step("Кнопка сохранения"):
        page_change_descr.btn_save()

    with allure.step("Проверка текущего описания на странице репозитория"):
        assert page_change_descr.get_descr() == "Новое описание"

    page_delete_repo = PageRepo(driver)

    with allure.step("Кнопка перехода в настройки репозитория"):
        page_delete_repo.btn_settings()

    with allure.step("Кнопка удаления репозитория"):
        page_delete_repo.btn_delete()

    with allure.step("Кнопка подтверждения удаления"):
        page_delete_repo.btn_delete_access()

    with allure.step("Кнопка подтверждения о прочтении последствий удаления"):
        page_delete_repo.btn_read_access()

    with allure.step("Поле ввода владельца и названия"):
        page_delete_repo.delete_repo_confirm()

    with allure.step("Удаление"):
        page_delete_repo.btn_delete_confirm()

    with allure.step("Проверка наличия сообщения об успешном удалении"):
        assert "Diploma_project_test" in page_delete_repo.alert_message()


@allure.title("Создание задачи")
@allure.description(
    "Тест проверяет создание задач"
)
@allure.feature("GitHub")
@allure.severity(allure.severity_level.NORMAL)
def test_create_issue(driver: webdriver.Chrome) -> None:
    """
    Тест проверяет создание задач в репозитории в GitHub
    :param driver: WebDriver - объект драйвера, переданный фикстурой
    :return: None
    """
    page_open_gh = PageAuth(driver)

    with allure.step("Открытие главной страницы GitHub"):
        page_open_gh.open_gh()

    page_create_repo = PageRepo(driver)

    with allure.step("Нажатие на кнопку создания"):
        page_create_repo.btn_create()

    with allure.step("Кнопка перехода к созданию репозитория"):
        page_create_repo.btn_new_repo()

    with allure.step("Ввод имени репозитория"):
        page_create_repo.input_name_repo("Diploma_project_issue")

    with allure.step("Нажатие на кнопку создания репозитория"):
        page_create_repo.btn_create_repo()

    page_create_issue = PageRepo(driver)

    with allure.step("Кнопка с задачами"):
        page_create_issue.btn_issue()

    with allure.step("Кнопка создания новой задачи"):
        page_create_issue.new_issue_btn()

    with allure.step("Поле ввода названия задачи"):
        page_create_issue.title_issue("Новая задача")

    with allure.step("Кнопка создания задачи"):
        page_create_issue.create_issue()

    with allure.step("Проверка актуального имени задачи"):
        assert page_create_issue.actual_title() == "Новая задача"

    page_delete_repo = PageRepo(driver)

    with allure.step("Кнопка перехода в настройки репозитория"):
        page_delete_repo.btn_settings()

    with allure.step("Кнопка удаления репозитория"):
        page_delete_repo.btn_delete()

    with allure.step("Кнопка подтверждения удаления"):
        page_delete_repo.btn_delete_access()

    with allure.step("Кнопка подтверждения о прочтении последствий удаления"):
        page_delete_repo.btn_read_access()

    with allure.step("Поле ввода владельца и названия"):
        page_delete_repo.delete_repo_confirm()

    with allure.step("Удаление"):
        page_delete_repo.btn_delete_confirm()

    with allure.step("Проверка наличия сообщения об успешном удалении"):
        assert "Diploma_project_issue" in page_delete_repo.alert_message()


@allure.title("Удаление репозитория")
@allure.description(
    "Тест проверяет удаление репозитория"
)
@allure.feature("GitHub")
@allure.severity(allure.severity_level.NORMAL)
def test_delete_repo(driver: webdriver.Chrome) -> None:
    """
    Тест проверяет удаление репозитория в GitHub
    :param driver: WebDriver - объект драйвера, переданный фикстурой
    :return: None
    """
    page_open_gh = PageAuth(driver)

    with allure.step("Открытие главной страницы GitHub"):
        page_open_gh.open_gh()

    page_create_repo = PageRepo(driver)

    with allure.step("Нажатие на кнопку создания"):
        page_create_repo.btn_create()

    with allure.step("Кнопка перехода к созданию репозитория"):
        page_create_repo.btn_new_repo()

    with allure.step("Ввод имени репозитория"):
        page_create_repo.input_name_repo("Diploma_project_delete")

    with allure.step("Нажатие на кнопку создания репозитория"):
        page_create_repo.btn_create_repo()

    page_delete_repo = PageRepo(driver)

    with allure.step("Кнопка перехода в настройки репозитория"):
        page_delete_repo.btn_settings()

    with allure.step("Кнопка удаления репозитория"):
        page_delete_repo.btn_delete()

    with allure.step("Кнопка подтверждения удаления"):
        page_delete_repo.btn_delete_access()

    with allure.step("Кнопка подтверждения о прочтении последствий удаления"):
        page_delete_repo.btn_read_access()

    with allure.step("Поле ввода владельца и названия"):
        page_delete_repo.delete_repo_confirm()

    with allure.step("Удаление"):
        page_delete_repo.btn_delete_confirm()

    with allure.step("Проверка наличия сообщения об успешном удалении"):
        assert "Diploma_project_delete" in page_delete_repo.alert_message()
