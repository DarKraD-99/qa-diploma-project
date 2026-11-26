import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import TimeoutException


class PageRepo:

    def __init__(self, driver: WebDriver) -> None:
        """
        Конструктор класса PageRepo
        :param driver: WebDriver - объект драйвера Selenium
        :return: None
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Нажатие на кнопку создания")
    def btn_create(self) -> None:
        """
        Нажатие на кнопку создания
        :return: None
        """
        self.wait.until(EC.element_to_be_clickable(
            (By.ID, "_R_mf9_")
            )).click()

    @allure.step("Переход к созданию репозитория")
    def btn_new_repo(self) -> None:
        """
        Нажатие на кнопку перехода к созданию репозитория
        :return: None
        """
        self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//span[text()='New repository']")
        )).click()

    @allure.step("Ввод имени репозитория")
    def input_name_repo(self, name: str) -> None:
        """
        Вводит имя репозитория
        :param name: str - имя репозитория
        :return: None
        """
        repo_name = self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "#repository-name-input")
            ))
        repo_name.send_keys(name)

        self.wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "#RepoNameInput-is-available")
        ))

    @allure.step("Ввод описания репозитория")
    def input_desc_repo(self, desc: str) -> None:
        """
        Вводит описание репозитория
        :param desc: str - описание репозитория
        :return: None
        """
        desc_repo = self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "input[name='Description']")
        ))
        desc_repo.send_keys(desc)

    @allure.step("Нажатие на кнопку создания репозитория")
    def btn_create_repo(self) -> None:
        """
        Нажатие на кнопку создания репозитория
        :return: None
        """
        btn_create = self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button[type='submit']")
        ))
        btn_create.click()

    @allure.step("Добавление файла README")
    def btn_readme(self) -> None:
        """
        Кнопка создания файла README в репозитории
        :return: None
        """
        readme_btn = self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button[aria-labelledby='add-readme']")
        ))
        readme_btn.click()

    @allure.step("Актуальное имя репозитория")
    def actual_name(self) -> str:
        """
        Актуальное имя репозитория
        :return: str
        """
        return self.wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "[data-testid='repo-name-link']")
        )).text

    @allure.step("Кнопка, открывающая раздел 'About' внутри репозитория")
    def btn_edit(self) -> None:
        """
        Кнопка открытия раздела 'About'
        :return: None
        """
        edit_btn = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "(//button[@aria-label='Edit repository metadata'])[2]")
        ))
        edit_btn.click()

    @allure.step("Ввод описания репозитория")
    def input_descr(self, description: str = "Новое описание") -> None:
        """
        Вводит описание репозитория в модальном окне About
        :param description: str - новое описание репозитория
        :return: None
        """
        descr_input = self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "input[placeholder*='description']")
        ))
        descr_input.click()

        descr_input.send_keys(Keys.CONTROL, "a")
        descr_input.send_keys(Keys.BACKSPACE)
        descr_input.send_keys(description)

    @allure.step("Кнопка сохранения изменений в разделе 'About'")
    def btn_save(self) -> None:
        """
        Кнопка сохранения изменений в разделе 'About'
        :return: None
        """
        save_btn = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[.//span[text()='Save changes']]")
        ))
        save_btn.click()
        self.wait.until(EC.invisibility_of_element(save_btn))

    @allure.step("Получение описания репозитория")
    def get_descr(self) -> str:
        """
        Получение описания репозитория
        :return: str
        """
        return self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, "(//p[contains(@class, 'SidebarAbout-module')])[2]")
        )).text

    @allure.step("Переход в раздел Issues")
    def btn_issue(self) -> None:
        """
        Кнопка перехода в раздел с задачами
        :return: None
        """
        issues_btn = self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "a[data-tab-item='issues']")
        ))
        issues_btn.click()

    @allure.step("Кнопка создания новой задачи")
    def new_issue_btn(self) -> None:
        """
        Кнопка создания новой задачи в репозитории
        :return: None
        """
        new_issue_btn = self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "a[href$='/issues/new/choose']")
        ))
        self.driver.execute_script(
            "arguments[0].removeAttribute('target');", new_issue_btn
        )
        new_issue_btn.click()

    @allure.step("Проверка загрузки страницы задач")
    def refresh_issues(self) -> None:
        """
        Проверка загрузки страницы Issues.
        Если кнопка создания задач не появилась, обновляет страницу.
        :return: None
        """
        try:
            self.wait.until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, "a[href$='/issues/new/choose']")
                )
            )
        except TimeoutException:
            self.driver.refresh()
            self.wait.until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, "a[href$='/issues/new/choose']")
                )
            )

    @allure.step("Поле ввода названия задачи")
    def title_issue(self, title: str) -> None:
        """
        Вводит название новой задачи
        :param title: str - название задачи
        :return: None
        """
        issue_title = self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "input[aria-label='Add a title']")
        ))
        issue_title.send_keys(title)

    @allure.step("Кнопка подтверждения создания задачи")
    def create_issue(self) -> None:
        """
        Нажатие кнопки создания задачи
        :return: None
        """
        issue_create = self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button[data-testid='create-issue-button']")
        ))
        issue_create.click()

    @allure.step("Текущее название задачи")
    def actual_title(self) -> str:
        """
        Актуальное название задачи
        :return: str
        """
        return self.wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "bdi[data-testid='issue-title']")
        )).text

    @allure.step("Кнопка перехода в настройки репозитория")
    def btn_settings(self) -> None:
        """
        Кнопка перехода в настройки репозитория
        :return: None
        """
        settings_btn = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[@data-tab-item='settings']")
        ))
        settings_btn.click()

    @allure.step("Кнопка перехода к удалению репозитория")
    def btn_delete(self) -> None:
        """
        Кнопка перехода к удалению репозитория
        :return: None
        """
        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);"
        )

        delete_btn = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[@id='dialog-show-repo-delete-menu-dialog']")
        ))
        delete_btn.click()

    @allure.step("Кнопка подтверждения удаления")
    def btn_delete_access(self) -> None:
        """
        Кнопка подтверждения удаления репозитория
        :return: None
        """
        delete_access_btn = self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button[id='repo-delete-proceed-button']")
        ))
        delete_access_btn.click()

    @allure.step("Кнопка подтверждения о прочтении последствий удаления")
    def btn_read_access(self) -> None:
        """
        Кнопка подтверждения о прочтении последствий удаления репозитория
        :return: None
        """
        read_access_btn = self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button[id='repo-delete-proceed-button']")
        ))
        read_access_btn.click()

    @allure.step("Ввод имени пользователя и названия")
    def delete_repo_confirm(self) -> None:
        """
        Ввод имени пользователя и названия репозитория
        :return: None
        """
        input_box = self.wait.until(EC.presence_of_element_located(
            (By.ID, "verification_field")
        ))

        repo_full_name = self.wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "#repo-delete-warning-container p.text-bold")
        )).text

        input_box.send_keys(repo_full_name)

    @allure.step("Кнопка подтверждения удаления")
    def btn_delete_confirm(self) -> None:
        """
        Кнопка подтверждения удаления репозитория
        :return: None
        """
        confirm_delete_btn = self.wait.until(EC.element_to_be_clickable(
            (By.ID, "repo-delete-proceed-button")
        ))
        confirm_delete_btn.click()

    @allure.step("Сообщение об успешном удалении")
    def alert_message(self) -> str:
        """
        Сообщение об успешном удалении репозитория
        :return: str
        """
        return self.wait.until(EC.visibility_of_element_located(
            (By.CLASS_NAME, "js-flash-alert")
        )).text
