import pytest
from selenium.webdriver.common.by import By

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: en, ru, es, etc.")

@pytest.fixture(scope="function")
def browser():
    # Здесь можно будет добавить конфигурацию браузера
    pass