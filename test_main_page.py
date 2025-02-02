# === Два подхода к переходам между страницами ===
# 1. Первый подход: Используем возвращаемое значение из go_to_login_page.
#    Раскомментируйте соответствующие строки в тесте для использования первого подхода.
#
# 2. Второй подход: Явно инициализируем LoginPage в тесте.
#    Это основной вариант. Оставьте эти строки активными для второго подхода.

import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    main_page = MainPage(browser, link)
    main_page.open()

    # === Первый подход: Используем возвращаемое значение из go_to_login_page ===
    # Раскомментируйте следующие строки для первого подхода
    # login_page = main_page.go_to_login_page()
    # login_page.should_be_login_page()

    # === Второй подход: Явно инициализируем LoginPage в тесте ===
    # Раскомментируйте следующие строки для второго подхода
    main_page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()