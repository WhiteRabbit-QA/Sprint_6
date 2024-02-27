import allure
from locators.additional_locators import AdditionalLocators
from locators.footer_locators import FooterLocators
from locators.header_locators import HeaderLocators
from locators.home_page_locators import HomePageLocators
from pages.base_page import BasePage


class HomePage(BasePage):

    page_url = 'https://qa-scooter.praktikum-services.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step('Открыть главную страницу')
    def open_home_page(self):
        self.open_page(self.page_url)

    @allure.step('Нажать кнопку "Заказать" на странице')
    def click_button_order_on_page(self):
        self.scroll_and_click_on_element(HomePageLocators.ORDER_BUTTON_ON_PAGE)

    @allure.step('Нажать кнопку "Заказать" в хедере')
    def click_button_order_on_header(self):
        self.click_on_element(HeaderLocators.ORDER_BUTTON_ON_HEADER)

    @allure.step('Нажать любую из кнопок "Заказать"')
    def click_any_button_order(self, locator):
        if locator == HomePageLocators.ORDER_BUTTON_ON_PAGE:
            self.click_button_order_on_page()
        elif locator == HeaderLocators.ORDER_BUTTON_ON_HEADER:
            self.click_button_order_on_header()

    @allure.step('Нажать на логотип "Самокат"')
    def click_logo_scooter(self):
        element = self.find_clickable_element(HeaderLocators.LOGO_SCOOTER)
        element.click()

    @allure.step('Нажать на логотип "Яндекс"')
    def click_logo_yandex(self):
        element = self.find_clickable_element(HeaderLocators.LOGO_YANDEX)
        element.click()

    @allure.step('Нажать на вопрос и получить текст ответа')
    def get_text_answer_for_ich_question(self, n):
        loc_question = self.format_locator(HomePageLocators.QUESTIONS, n)
        self.click_on_element(loc_question)
        loc_answer = self.format_locator(HomePageLocators.ANSWERS, n)
        text_answer = self.get_text_from_element(loc_answer)
        return text_answer

    @allure.step('Проверить заголовок страницы')
    def check_title_page(self):
        text = self.get_text_from_element(HomePageLocators.HOME_TITLE)
        return "на пару дней" in text

    @allure.step('Нажать кнопку "да все привыкли"')
    def click_cookies_button(self):
        self.scroll_and_click_on_element(FooterLocators.COOKIES_BUTTON)

    @allure.step('Получить url нового окна')
    def get_url_new_window(self):
        self.find_visibility_element(AdditionalLocators.TITLE_MODAL_DZEN)
        return self.get_url()
