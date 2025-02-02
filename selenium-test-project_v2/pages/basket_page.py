from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_empty_basket(self):
        """Проверяет, что корзина пуста"""
        assert self.is_not_element_present(*BasketPageLocators.PRODUCTS_IN_BASKET), \
            "Products are present in the basket, but should not be"

    def should_be_empty_basket_message(self):
        """Проверяет наличие сообщения о том, что корзина пуста"""
        empty_message = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE).text
        assert "Your basket is empty" in empty_message, \
            f"Empty basket message is not presented or incorrect: {empty_message}"