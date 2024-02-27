import allure
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from pages.home_page import HomePage


@allure.title('Открыть браузер')
@pytest.fixture(scope='function')
def driver():
    service = Service(executable_path=GeckoDriverManager().install())
    options = Options()
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Firefox(service=service, options=options)
    yield driver
    with allure.step("Закрыть браузер"):
        driver.quit()


@allure.title('Разрешить куки')
@pytest.fixture
def accept_cookies(driver):
    home = HomePage(driver)
    home.open_home_page()
    home.click_cookies_button()
