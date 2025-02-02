from .base_page import BasePage
from .locators import ProductPageLocators
import math
from selenium.common.exceptions import NoAlertPresentException

class ProductPage(BasePage):
    def add_product_to_basket(self):
        """Добавляет товар в корзину"""
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()

    def solve_quiz_and_get_code(self):
        """Решает математическую задачу и получает проверочный код"""
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def get_product_name(self):
        """Возвращает название товара"""
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        """Возвращает цену товара"""
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def should_be_product_added_message(self, product_name):
        """Проверяет сообщение о добавлении товара"""
        message = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text
        assert product_name in message, f"Product name not found in message: {product_name} not in {message}"

    def should_be_basket_total_message(self, product_price):
        """Проверяет сообщение со стоимостью корзины"""
        basket_total = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_MESSAGE).text
        assert product_price in basket_total, f"Basket total does not match the product price: {product_price} not in {basket_total}"

    def should_not_be_success_message(self):
        """Проверяет, что нет сообщения об успехе после добавления товара в корзину"""
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_message_disappear_after_adding_product_to_basket(self):
        """Проверяет, что сообщение об успехе исчезает после добавления товара в корзину"""
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message did not disappear"