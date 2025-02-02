from selenium.webdriver.common.by import By

class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a.btn-default")  # Локатор для кнопки корзины
class MainPageLocators:
    MAIN_PAGE_URL = (By.CSS_SELECTOR, ".page-header")  # Пример локатора для главной страницы
class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success:nth-child(1) strong")
    BASKET_TOTAL_MESSAGE = (By.CSS_SELECTOR, ".alert-info strong")

class BasketPageLocators:
    PRODUCTS_IN_BASKET = (By.CSS_SELECTOR, ".basket-items")  # Локатор для товаров в корзине
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")  # Локатор для сообщения о пустой корзине