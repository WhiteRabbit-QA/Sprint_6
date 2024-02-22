import allure
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
from locators.footer_locators import FooterLocators


@allure.title('Открыть браузер')
@pytest.fixture(scope='function')
def driver():
    service = Service(executable_path=GeckoDriverManager().install())
    options = Options()
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Firefox(service=service, options=options)
    driver.get("https://qa-scooter.praktikum-services.ru/")
    yield driver
    with allure.step("Закрыть браузер"):
        driver.quit()


@allure.title('Разрешить cookies')
@pytest.fixture
def click_cookies_button(driver):
    cookie_button = WebDriverWait(driver, 4).until(EC.element_to_be_clickable(FooterLocators.COOKIES_BUTTON))
    cookie_button.click()
