import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from config import GITHUB_URL, GITHUB_LOGIN, GITHUB_PASSWORD


class PageAuth:

    def __init__(self, driver: WebDriver) -> None:
        """
        Конструктор класса PageAuth
        :param driver: WebDriver - объект драйвера Selenium
        :return: None
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.driver.maximize_window()

    @allure.step("Открытие главной страницы GitHub")
    def open_gh(self) -> None:
        """
        Открывает главную страницу GitHub
        :return: None
        """
        self.driver.get(GITHUB_URL)

    @allure.step("Переход на страницу авторизации")
    def sign_in_button(self) -> None:
        """
        Переход на страницу авторизации GitHub
        :return: None
        """
        sign_in = self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, ".signInWrap___-hg2x")
            ))
        sign_in.click()

    @allure.step("Ввод логина")
    def input_login(self) -> None:
        """
        Вводит логин пользователя в соответствующее поле
        :return: None
        """
        login_input = self.wait.until(EC.presence_of_element_located(
            (By.ID, "login_field")
        ))
        login_input.clear()
        login_input.send_keys(GITHUB_LOGIN)

    @allure.step("Ввод пароля")
    def input_password(self) -> None:
        """
        Вводит пароль пользователя в соответствующее поле
        :return: None
        """
        password_input = self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "#password")
        ))
        password_input.send_keys(GITHUB_PASSWORD)

    @allure.step("Нажатие на кнопку авторизации")
    def click_auth_btn(self) -> None:
        """
        Нажимает кнопку авторизации
        :return: None
        """
        auth_btn = self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "input[value='Sign in']")
            ))
        auth_btn.click()
