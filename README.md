**ЯндексПрактикум. Курс "Автоматизатор тестирования на Python".** 
---
**Спринт 6 "Page Object"**
***
В проекте подготовлены автотесты с применением паттерна POM для сервиса [Яндекс.Самокат](https://qa-scooter.praktikum-services.ru/).
Также прикреплен отчет о результатах прохождения тестов.

### Тестируется функциональность страниц сайта:

****Главная страница - выпадающий список раздела "Вопросы о важном"****
* `test_correct_answers_for_questions` - получение ответа при клике на вопрос

***Страница заказа - заказ самоката, переходы по клику на логотипы***
* `test_create_new_order_with_two_order_button` - создание заказа через две точки входа: кнопка "Заказать" в хедере и внизу страницы
* `test_click_logo_scooter_after_new_order` - проверка перехода на главную страницу по клику на лого "Самокат" после оформления заказа
* `test_click_logo_yandex_after_new_order` - проверка редиректа на страницу "Дзен" по клику на лого "Яндекс" после оформления заказа'

***
### Структура проекта
Пакет `locators`: модули с локаторами страниц
* footer_locators.py (локаторы футера)
* header_locators.py (локаторы хедера)
* home_page_locators.py (локаторы главной страницы)
* order_page_locators.py (локаторы страницы заказа)

Пакет `pages`: модули с методами страниц
* base_page.py (общие методы страниц)
* home_page.py (главная страница)
* order_page.py (страница заказа)

Пакет `tests`: модули с тестами
* test_home_page.py
* test_order_page.py

В модуле `conftest.py` реализованы фикстуры:

* driver - инициализация браузера Mozilla Firefox
* click_cookies_button - разрешение сохранения cookies

Тестовые данные:
* `data.py`

Отчёты в формате JSON хранятся в директории `allure_results`
***
### Для запуска тестов
* Подключить Selenium
```
pip install selenium
```
* Для автоматической установки и обновления веб-драйвера установить Webdriver Manager
```
pip install webdriver_manager
```
* Установить pytest
```
pip install pytest
```
* Запуск всех тестов с сохранением отчета
```
pytest -vs --alluredir=allure_results
```
* Сгенерировать отчет о тестировании в формате веб-страницы
```
allure serve allure_results
```
