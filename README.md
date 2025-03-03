# Автоматизация тестирования интернет-магазина с использованием Selenium и Page Object

Этот проект представляет собой набор автоматизированных тестов для проверки функциональности интернет-магазина. Тесты написаны с использованием фреймворка **pytest** и паттерна **Page Object**, что обеспечивает чистый, модульный и поддерживаемый код.

---

## **Описание проекта**

Проект включает тесты для проверки следующих сценариев:
1. Регистрация нового пользователя.
2. Добавление товаров в корзину как гостем, так и зарегистрированным пользователем.
3. Проверка отображения сообщений об успешном добавлении товара.
4. Переход на страницу логина и регистрации.
5. Проверка пустой корзины.

Тесты разбиты по категориям и помечены метками для удобства запуска:
- `@pytest.mark.need_review`: Тесты, которые требуют проверки.
- `@pytest.mark.user_add_to_basket`: Тесты для проверки добавления товаров в корзину зарегистрированными пользователями.

---

## **Структура проекта**
selenium-test-project_v2/

├── pages/ # Классы страниц (Page Objects)

│ ├── init .py

│ ├── base_page.py # Базовый класс для всех страниц

│ ├── basket_page.py # Страница корзины

│ ├── locators.py # Локаторы элементов

│ ├── login_page.py # Страница логина/регистрации

│ ├── main_page.py # Главная страница

│ └── product_page.py # Страница товара

├── test_main_page.py # Тесты для главной страницы

├── test_product_page.py # Тесты для страницы товара

├── conftest.py # Фикстуры pytest

├── pytest.ini # Настройки pytest

├── requirements.txt # Зависимости проекта

└── README.md # Это файл


---

## **Как запустить проект**

### ** Установите зависимости**

Убедитесь, что у вас установлен Python 3.8 или выше. Затем установите необходимые зависимости:

```bash
pip install -r requirements.txt

2. Запустите тесты
Для запуска всех тестов выполните команду:

pytest -v --tb=line --language=en

Дополнительные параметры:
Выбор языка интерфейса: Используйте параметр --language, чтобы указать язык интерфейса браузера. Например:

pytest -v --tb=line --language=ru

Запуск тестов с меткой: Запустите только тесты, помеченные меткой need_review:

pytest -v --tb=line --language=en -m need_review

3. Параллельный запуск тестов (опционально)
Чтобы ускорить выполнение тестов, используйте плагин pytest-xdist для параллельного запуска:

pytest -n 2  # Запуск на 2 ядрах

Автор
Сергей Каманов : mr.kamanov@yandex.ru

