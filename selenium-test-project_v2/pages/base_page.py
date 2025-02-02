from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from .locators import BasePageLocators  # Импортируем BasePageLocators

class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        """Открывает страницу"""
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        """Проверяет наличие элемента на странице"""
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        """Проверяет, что элемент не появляется на странице в течение заданного времени"""
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what, timeout=4):
        """Проверяет, что элемент исчезает со страницы в течение заданного времени"""
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(
                EC.presence_of_element_located((how, what))
            )
        except TimeoutException:
            return False
        return True

    def go_to_login_page(self):
        """Переходит на страницу логина"""
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)  # Используем BasePageLocators
        link.click()

    def should_be_login_link(self):
        """Проверяет наличие ссылки на страницу логина"""
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"