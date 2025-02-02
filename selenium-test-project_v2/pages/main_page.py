from .base_page import BasePage
from .locators import MainPageLocators

class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    def should_be_main_page(self):
        """Проверяет, что текущая страница является главной"""
        assert "catalogue" in self.browser.current_url, "This is not the main page"