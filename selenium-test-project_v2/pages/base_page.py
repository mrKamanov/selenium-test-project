from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from .locators import BasePageLocators

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

    def should_be_authorized_user(self):
        """Проверяет, что пользователь залогинен"""
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"

    def go_to_login_page(self):
        """Переходит на страницу логина"""
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_login_link(self):
        """Проверяет наличие ссылки на страницу логина"""
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def go_to_basket_page(self):
        """Переходит на страницу корзины"""
        basket_link = self.browser.find_element(*BasePageLocators.BASKET_LINK)
        basket_link.click()