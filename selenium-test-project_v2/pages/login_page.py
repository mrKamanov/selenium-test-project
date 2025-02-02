from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def register_new_user(self, email, password):
        """Регистрирует нового пользователя"""
        email_input = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        email_input.send_keys(email)
        password_input = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD)
        password_input.send_keys(password)
        confirm_password_input = self.browser.find_element(*LoginPageLocators.REGISTER_CONFIRM_PASSWORD)
        confirm_password_input.send_keys(password)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()
    def should_be_login_page(self):
        """Проверяет, что это страница логина"""
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        """Проверяет, что текущий URL содержит 'login'"""
        assert "login" in self.browser.current_url, "URL does not contain 'login'"

    def should_be_login_form(self):
        """Проверяет наличие формы входа"""
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        """Проверяет наличие формы регистрации"""
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"