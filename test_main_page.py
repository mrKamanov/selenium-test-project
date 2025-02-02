import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    main_page = MainPage(browser, link)
    main_page.open()
    main_page.go_to_login_page()  # Переходим на страницу логина

    # Явно инициализируем объект LoginPage
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()  # Проверяем, что это страница логина

def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()