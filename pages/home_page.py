from locators.header_locators import HeaderLocators
from locators.home_page_locators import HomePageLocators
from pages.base_page import Base


class HomePage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Нажать кнопку "Заказать"" на странице
    def click_button_order_on_page(self):
        self.scroll_and_click_on_element(HomePageLocators.ORDER_BUTTON_ON_PAGE)

    # Нажать любую из кнопок "Заказать" (на странице, в хедере)
    def click_any_button_order(self, locator):
        if locator == HomePageLocators.ORDER_BUTTON_ON_PAGE:
            self.click_button_order_on_page()
        elif locator == HeaderLocators.ORDER_BUTTON_ON_HEADER:
            self.click_button_order_on_header()

    # Получить текст ответа для любого вопроса
    def get_text_answer_for_ich_question(self, locator_q, locator_a, n):
        loc_question = self.format_locator(locator_q, n)
        self.click_on_element(loc_question)
        loc_answer = self.format_locator(locator_a, n)
        text_answer = self.get_text_from_element(loc_answer)
        return text_answer

    # Проверка заголовка страницы
    def check_title_page(self):
        text = self.get_text_from_element(HomePageLocators.HOME_TITLE)
        return "на пару дней" in text
