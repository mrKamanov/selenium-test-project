from selenium.webdriver.common.by import By

class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a.btn-default")  # Локатор для кнопки корзины
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")  # Локатор для иконки пользователя

class MainPageLocators:
    MAIN_PAGE_URL = (By.CSS_SELECTOR, ".page-header")  # Пример локатора для главной страницы

class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")  # Локатор для формы логина
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")  # Локатор для формы регистрации
    REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")  # Поле ввода email для регистрации
    REGISTER_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")  # Поле ввода пароля для регистрации
    REGISTER_CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")  # Подтверждение пароля
    REGISTER_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")  # Кнопка регистрации

class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")  # Кнопка "Добавить в корзину"
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")  # Название товара
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")  # Цена товара
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success:nth-child(1) strong")  # Сообщение об успешном добавлении
    BASKET_TOTAL_MESSAGE = (By.CSS_SELECTOR, ".alert-info strong")  # Сообщение о стоимости корзины

class BasketPageLocators:
    PRODUCTS_IN_BASKET = (By.CSS_SELECTOR, ".basket-items")  # Локатор для товаров в корзине
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")  # Локатор для сообщения о пустой корзине