from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    main_page = MainPage(browser, link)
    main_page.open()
    # === Первый подход: Используем возвращаемое значение из go_to_login_page ===
    # Если вы хотите использовать первый подход, раскомментируйте следующие строки:
    # login_page = main_page.go_to_login_page()
    # login_page.should_be_login_page()
    # === Второй подход: Явно инициализируем LoginPage в тесте ===
    # Это основной вариант. Оставьте эти строки активными для второго подхода:
    main_page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

# Новый тест: проверка пустой корзины с главной страницы
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_page()  # Переходим в корзину
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()  # Проверяем, что корзина пуста
    basket_page.should_be_empty_basket_message()  # Проверяем сообщение о пустой корзине