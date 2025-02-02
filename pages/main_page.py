# === Два подхода к переходам между страницами ===
# 1. Первый подход: Метод go_to_login_page возвращает объект LoginPage.
#    Для его использования раскомментируйте импорт LoginPage и строку return LoginPage(...) в методе go_to_login_page.
#
# 2. Второй подход: Переход происходит неявно, страница инициализируется в тесте.
#    Это основной вариант. Оставьте метод go_to_login_page без return и используйте явную инициализацию в тестах.

from .base_page import BasePage
from .locators import MainPageLocators
# Для первого подхода импортируем LoginPage
# from .login_page import LoginPage

class MainPage(BasePage):
    def go_to_login_page(self):
        """Переходит на страницу логина"""
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

        # === Первый подход: Возвращаем объект LoginPage ===
        # Раскомментируйте следующую строку для первого подхода
        # return LoginPage(browser=self.browser, url=self.browser.current_url)

    def should_be_login_link(self):
        """Проверяет наличие ссылки на логин"""
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"