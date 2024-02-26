import allure
from selenium.webdriver import Keys
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage
from datetime import datetime, timedelta


class OrderPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @staticmethod
    def calculate_correct_date(cnt_days_from_today):
        calculation_date = datetime.today() + timedelta(days=cnt_days_from_today)
        return calculation_date.strftime("%d.%m.%Y")

    @allure.step('Ввести в поле имя')
    def set_name(self, user_name):
        self.fill_input(OrderPageLocators.FIELD_NAME, user_name)

    @allure.step('Ввести в поле фамилию')
    def set_surname(self, user_surname):
        self.fill_input(OrderPageLocators.FIELD_SURNAME, user_surname)

    @allure.step('Ввести в поле адрес доставки')
    def set_address(self, address):
        self.fill_input(OrderPageLocators.FIELD_ADDRESS, address)

    @allure.step('Выбрать станцию метро')
    def set_metro_station(self, station):
        click_drop = self.find_clickable_element(OrderPageLocators.FIELD_METRO_STATION)
        click_drop.click()
        choose_station = self.format_locator(OrderPageLocators.STATIONS, station)
        self.click_on_element(choose_station)

    @allure.step('Ввести в поле номер телефона')
    def set_telephone(self, telephone):
        self.fill_input(OrderPageLocators.FIELD_TELEPHONE_NUMBER, telephone)

    @allure.step('Ввести в поле дату доставки')
    def set_date_rental(self, cnt_days_from_today):
        choose_date = self.calculate_correct_date(cnt_days_from_today)
        click_drop = self.find_clickable_element(OrderPageLocators.FIELD_CALENDAR)
        click_drop.click()
        click_drop.send_keys(choose_date)
        click_drop.send_keys(Keys.ENTER)

    @allure.step('Выбрать количество дней аренды')
    def set_count_rental_days(self, index):
        self.click_on_element(OrderPageLocators.FIELD_RENTAL_DAYS)
        choose_cnt_days = self.format_locator(OrderPageLocators.DAYS, index)
        self.click_on_element(choose_cnt_days)

    @allure.step('Выбрать цвет самоката')
    def set_color_scooter(self, color):
        choose_color = None
        if color == "чёрный жемчуг":
            choose_color = self.format_locator(OrderPageLocators.COLORS, "'black'")
        elif color == "серая безысходность":
            choose_color = self.format_locator(OrderPageLocators.COLORS, "'grey'")
        self.click_on_element(choose_color)

    @allure.step('Ввести в поле комментарий')
    def set_comment(self, comment):
        self.fill_input(OrderPageLocators.FIELD_COMMENT, comment)

    @allure.step('Нажать кнопку "Далее"')
    def click_button_next(self):
        self.click_on_element(OrderPageLocators.BUTTON_NEXT)

    @allure.step('Нажать кнопку "Заказать"')
    def click_button_order(self):
        self.click_on_element(OrderPageLocators.BUTTON_ORDER)

    @allure.step('Нажать кнопку "Да"')
    def click_button_yes(self):
        self.click_on_element(OrderPageLocators.BUTTON_YES)

    @allure.step('Нажать кнопку "Посмотреть статус"')
    def click_button_look_status_order(self):
        self.click_on_element(OrderPageLocators.BUTTON_STATUS_ORDER)

    @allure.step('Создать новый заказ')
    def create_new_order(self, user_name, user_surname, address, station, telephone, cnt_days_from_today, index, color, comment):
        self.set_name(user_name)
        self.set_surname(user_surname)
        self.set_address(address)
        self.set_metro_station(station)
        self.set_telephone(telephone)
        self.click_button_next()
        self.set_date_rental(cnt_days_from_today)
        self.set_count_rental_days(index)
        self.set_color_scooter(color)
        self.set_comment(comment)
        self.click_button_order()
        self.click_button_yes()

    @allure.step('Завершить оформление заказа')
    def complete_create_new_order(self, user_name, user_surname, address, station, telephone, cnt_days_from_today,
                                  index, color, comment):
        self.create_new_order(user_name, user_surname, address, station, telephone, cnt_days_from_today, index, color, comment)
        self.click_button_look_status_order()

    @allure.step('Проверить заголовок модального окна "Заказ оформлен"')
    def check_title_order_modal(self):
        text = self.get_text_from_element(OrderPageLocators.TITLE_ORDER_MODAL)
        return "Заказ оформлен" in text
