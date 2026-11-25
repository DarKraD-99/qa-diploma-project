# Дипломный проект по профессии QA

## Описание проекта

Дипломный проект по тестированию веб-приложения GitHub

Проект включает в себя UI- и API-автотесты, проверяющие основные функции GitHub

## Используемые технологии

- Python
- Pytest
- Requests
- Selenium WebDriver
- Allure Report
- Test IT

## Форматирование кода

- Коды форматируются в соответствии с PEP 8 (стиль написания кода на Python).
- Для документирования методов и функций используются docstrings.
- Все шаги теста размечены с помощью @allure.step или with allure.step(...) для улучшения читаемости отчётов.

## Структура проекта

```bash
qa-diploma-project/
├── tests/
│   ├── api/
│   │   └── test_api_github.py
│   └── ui/
│       ├── pages/
│       │   ├── PageAuth.py
│       │   └── PageRepo.py
│       └── test_ui_github.py
├── .env
├── .gitignore
├── config.py
├── connection_config.ini
├── pytest.ini
├── requirements.txt
└── README.md
```

Файлы ".env" и "connection_config.ini" необходимо создать самостоятельно. Не размещайте реальные токены и пароли в публичном репозитории.

## Установка проекта

1. Клонировать репозиторий:

```bash
git clone <ссылка-на-репозиторий>
```

2. Перейти в папку проекта:

```bash
cd qa-diploma-project
```

3. Установить зависимости:

```bash
pip install -r requirements.txt
```

4. Создать файл .env и указать настройки GitHub:

```bash
GITHUB_API_URL=https://api.github.com
GITHUB_URL=https://github.com
GITHUB_TOKEN=your_token
GITHUB_LOGIN=your_login
GITHUB_PASSWORD=your_password
```

5. Настроить connection_config.ini для подключения к Test IT

## Запуск автотестов

- Запуск всех API-тестов:

```bash
pytest -s -v -m api
```

- Запуск всех UI-тестов

```bash
pytest -s -v -m ui
```

- Запуск всех тестов

```bash
pytest -s -v
```

## Инструкция по запуску тестов для формирования отчета Allure

1. Установите необходимые зависимости:

```bash
pip install -r requirements.txt
```

2. Запустите тесты с генерацией отчёта Allure:

```bash
pytest -s -v --alluredir=allure-results
```

Команда запустит все тесты и сохранит результаты в директорию allure-results.

## Инструкция по просмотру сформированного отчета Allure

1. После завершения тестов, чтобы посмотреть отчёт, выполните команду:

```bash
allure serve allure-results
```

Команда сформирует отчёт, запустит локальный сервер и откроет отчёт в браузере.

2. В отчёте Allure отображаются:

- Названия тестов
- Описание тестов и проверяемых функций
- Шаги выполнения тестов
- Результаты проверок
- Информация об ошибках с указанием ожидаемого и фактического результата

В рамках проекта отчёт содержит информацию о тестировании авторизации, создании, редактировании и удалении репозиториев, а также создании задач (Issues) в GitHub.

## Интеграция автотестов с Test IT

Для отправки результатов автотестов в Test IT используется testit-adapter-pytest.

Запуск API-тестов с отправкой результатов в Test IT:

```bash
pytest -s -v -m api --testit --tmsConfigFile=connection_config.ini
```

Запуск UI-тестов с отправкой результатов в Test IT:

```bash
pytest -s -v -m ui --testit --tmsConfigFile=connection_config.ini
```

Перед запуском необходимо настроить файл connection_config.ini, указав URL Test IT, ID проекта и ID конфигурации, а также задать переменную окружения TMS_PRIVATE_TOKEN с личным токеном доступа.

## Результаты проекта

В проекте реализовано 11 автоматизированных тестов:

- 6 API-тестов.
- 5 UI-тестов.

Для запуска и организации тестов используется Pytest, для формирования отчётов - Allure Report, для управления тестированием и хранения результатов прогонов - Test IT.