from selenium.webdriver import Keys
from datetime import datetime, timedelta
from locators.order_page_locators import OrderPageLocators
from pages.base_page import Base


class OrderPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Расчет любой даты от текущего дня включительно (для валидной даты доставки)
    @staticmethod
    def calculate_correct_date(cnt_days_from_today):
        calculation_date = datetime.today() + timedelta(days=cnt_days_from_today)
        return calculation_date.strftime("%d.%m.%Y")

    # Ввести имя клиента
    def set_name(self, user_name):
        self.fill_input(OrderPageLocators.FIELD_NAME, user_name)

    # Ввести фамилию клиента
    def set_surname(self, user_surname):
        self.fill_input(OrderPageLocators.FIELD_SURNAME, user_surname)

    # Ввести адрес доставки клиента
    def set_address(self, address):
        self.fill_input(OrderPageLocators.FIELD_ADDRESS, address)

    # Выбрать станцию метро
    def set_metro_station(self, station):
        click_drop = self.find_clickable_element(OrderPageLocators.FIELD_METRO_STATION)
        click_drop.click()
        choose_station = self.format_locator(OrderPageLocators.STATIONS, station)
        self.click_on_element(choose_station)

    # Ввести номер телефона
    def set_telephone(self, telephone):
        self.fill_input(OrderPageLocators.FIELD_TELEPHONE_NUMBER, telephone)

    # Ввести валидную дату доставки
    def set_date_rental(self, cnt_days_from_today):
        choose_date = self.calculate_correct_date(cnt_days_from_today)
        click_drop = self.find_clickable_element(OrderPageLocators.FIELD_CALENDAR)
        click_drop.click()
        click_drop.send_keys(choose_date)
        click_drop.send_keys(Keys.ENTER)

    # Выбрать количество дней аренды
    def set_count_rental_days(self, index):
        self.click_on_element(OrderPageLocators.FIELD_RENTAL_DAYS)
        choose_cnt_days = self.format_locator(OrderPageLocators.DAYS, index)
        self.click_on_element(choose_cnt_days)

    # Выбрать цвет самоката
    def set_color_scooter(self, color):
        choose_color = None
        if color == "чёрный жемчуг":
            choose_color = self.format_locator(OrderPageLocators.COLORS, "'black'")
        elif color == "серая безысходность":
            choose_color = self.format_locator(OrderPageLocators.COLORS, "'grey'")
        self.click_on_element(choose_color)

    def set_comment(self, comment):
        self.fill_input(OrderPageLocators.FIELD_COMMENT, comment)

    # нажать кнопку "Далее" (переход на форму "Про аренду")
    def click_button_next(self):
        self.click_on_element(OrderPageLocators.BUTTON_NEXT)

    # нажать кнопку "Заказать" (переход на модалку "Хотите оформить заказ?")
    def click_button_order(self):
        self.click_on_element(OrderPageLocators.BUTTON_ORDER)

    # Нажать кнопку "Да" (подтвердить заказ)
    def click_button_yes(self):
        self.click_on_element(OrderPageLocators.BUTTON_YES)

    # Нажать кнопку "Посмотреть статус"
    def click_button_look_status_order(self):
        self.click_on_element(OrderPageLocators.BUTTON_STATUS_ORDER)

    # Создать новый заказ
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

    # Завершить оформление заказа (переход на страницу созданного заказа)
    def complete_create_new_order(self, user_name, user_surname, address, station, telephone, cnt_days_from_today,
                                  index, color, comment):
        self.create_new_order(user_name, user_surname, address, station, telephone, cnt_days_from_today, index, color, comment)
        self.click_button_look_status_order()

    # Проверка заголовка модального окна "Заказ оформлен"
    def check_title_order_modal(self):
        text = self.get_text_from_element(OrderPageLocators.TITLE_ORDER_MODAL)
        return "Заказ оформлен" in text
