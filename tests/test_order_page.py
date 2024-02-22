import allure
import pytest
from selenium.webdriver.common.by import By
from locators.header_locators import HeaderLocators
from locators.home_page_locators import HomePageLocators
from pages.home_page import HomePage
from pages.order_page import OrderPage
from data import CorrectUserData


class TestOrderPage:

    @allure.story('Создание заказа')
    @allure.title('Проверка создания заказа через две точки входа: кнопка "Заказать" в хедере и внизу страницы')
    @pytest.mark.parametrize('locator',
                             [HeaderLocators.ORDER_BUTTON_ON_HEADER, HomePageLocators.ORDER_BUTTON_ON_PAGE])
    def test_create_new_order_with_two_order_button(self, driver, click_cookies_button, locator):
        home = HomePage(driver)
        order = OrderPage(driver)
        with allure.step('Нажать на кнопку "Заказать"'):
            home.click_any_button_order(locator)
        with allure.step('Создать заказ'):
            order.create_new_order(CorrectUserData.user_name[0], CorrectUserData.user_surname[1],
                                   CorrectUserData.address,
                                   CorrectUserData.metro_station[0], CorrectUserData.telephone[0],
                                   CorrectUserData.rental_date[0], CorrectUserData.cnt_rental_days[6],
                                   CorrectUserData.color_scooter[1], CorrectUserData.comment)
        assert order.check_title_order_modal()

    @allure.story('Клик на логотип после оформления заказа')
    @allure.title('Проверка перехода на главную страницу по клику на лого "Самокат" после оформления заказа')
    def test_click_logo_scooter_after_new_order(self, driver, click_cookies_button):
        home = HomePage(driver)
        order = OrderPage(driver)
        with allure.step('Нажать на кнопку "Заказать"'):
            home.click_button_order_on_page()
        with allure.step('Создать и подтвердить заказ'):
            order.complete_create_new_order(CorrectUserData.user_name[3], CorrectUserData.user_surname[1],
                                            CorrectUserData.address, CorrectUserData.metro_station[1],
                                            CorrectUserData.telephone[1], CorrectUserData.rental_date[1],
                                            CorrectUserData.cnt_rental_days[3], CorrectUserData.color_scooter[0],
                                            CorrectUserData.comment)
        with allure.step('Нажать на логотип "Самокат"'):
            order.click_logo_scooter()
        assert home.check_title_page()

    @allure.story('Клик на логотип после оформления заказа')
    @allure.title('Проверка редиректа на страницу "Дзена" по клику на лого "Яндекс" после оформления заказа')
    def test_click_logo_yandex_after_new_order(self, driver, click_cookies_button):
        home = HomePage(driver)
        order = OrderPage(driver)
        with allure.step('Нажать на кнопку "Заказать"'):
            home.click_button_order_on_page()
        with allure.step('Создать и подтвердить заказ'):
            order.complete_create_new_order(CorrectUserData.user_name[3], CorrectUserData.user_surname[1],
                                            CorrectUserData.address, CorrectUserData.metro_station[2],
                                            CorrectUserData.telephone[1], CorrectUserData.rental_date[2],
                                            CorrectUserData.cnt_rental_days[3], CorrectUserData.color_scooter[0],
                                            CorrectUserData.comment)
        with allure.step('Нажать на логотип "Яндекс"'):
            order.click_logo_yandex()
        with allure.step('Перейти на открывшуюся вкладку браузера'):
            order.switch_to_window(-1)
        order.find_visibility_element((By.XPATH, "//*[text()='Удобный и быстрый Яндекс Браузер с нейросетями']"))
        assert order.get_current_url() == "https://dzen.ru/?yredirect=true"
