import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: en, ru, es, etc.")

@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("--language")

    options = ChromeOptions()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})

    print(f"\nstart browser for test with language: {user_language}..")
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    yield browser
    print("\nquit browser..")
    browser.quit()