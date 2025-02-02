from selenium.webdriver.common.by import By

class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a.btn-default")  # Локатор для кнопки корзины
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")  # Локатор для иконки пользователя
class MainPageLocators:
    MAIN_PAGE_URL = (By.CSS_SELECTOR, ".page-header")  # Пример локатора для главной страницы
class LoginPageLocators:
    REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")

class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success:nth-child(1) strong")
    BASKET_TOTAL_MESSAGE = (By.CSS_SELECTOR, ".alert-info strong")

class BasketPageLocators:
    PRODUCTS_IN_BASKET = (By.CSS_SELECTOR, ".basket-items")  # Локатор для товаров в корзине
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")  # Локатор для сообщения о пустой корзине