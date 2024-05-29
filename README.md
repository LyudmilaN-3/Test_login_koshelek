# Test_login_koshelek

**в проекте реализованы негативные сценарии для страницы регистрации сервиса "Кошелек.ру" с использованием библиотек Selenium и Allure**

### Используемые технологии и библиотеки:

Allure

Selenium

pytest

### Установка и настройки:

Клонировать репозиторий и перейти в него в командной строке:

`git clone https://github.com/yandex-praktikum/Test_login_koshelek.git`

`cd Test_login_koshelek`

Cоздание и активация виртуального окружения:

`python -m venv venv`

`source venv/Scripts/activate`

Установка зависимостей из файла requirements.txt:

`python -m pip install --upgrade pip`

`pip install -r requirements.txt`

Запуск тестов с применением фреймворка Allure:

`pytest --alluredir=allure_results`

Генерация отчета в формате веб-страницы:

`allure serve allure_results`