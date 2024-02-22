from selenium.webdriver.common.by import By


class OrderPageLocators:
    # Заголовок формы заказа "Для кого самокат"
    TITLE_ORDER_FORM = [By.LINK_TEXT, "Для кого самокат"]

    # Поле "Имя"
    FIELD_NAME = [By.CSS_SELECTOR, "input[placeholder='* Имя']"]

    # Поле "Фамилия"
    FIELD_SURNAME = [By.CSS_SELECTOR, "input[placeholder='* Фамилия']"]

    # Поле "Адрес"
    FIELD_ADDRESS = [By.CSS_SELECTOR, "input[placeholder='* Адрес: куда привезти заказ']"]

    # Поле "Станция метро"
    FIELD_METRO_STATION = [By.CLASS_NAME, "select-search__input"]

    # Локатор всех станций метро
    STATIONS = [By.XPATH, "//*[@class='Order_Text__2broi' and text()={}]"]

    # Поле "Телефон"
    FIELD_TELEPHONE_NUMBER = [By.CSS_SELECTOR, "input[placeholder='* Телефон: на него позвонит курьер']"]

    # Кнопка "Далее"
    BUTTON_NEXT = [By.CSS_SELECTOR, "[class*='Button_Middle']"]

    # Поле "Когда привезти самокат"
    FIELD_CALENDAR = [By.CSS_SELECTOR, "[class='react-datepicker__input-container']>input"]

    # Поле "Срок аренды"
    FIELD_RENTAL_DAYS = [By.CSS_SELECTOR, "[class*='Dropdown-placeholder']"]

    # Локатор всех значений в выпадающем списке "Срок аренды"
    DAYS = [By.XPATH, "//*[@class='Dropdown-option' and text()={}]"]

    # Локатор для чек-боксов
    COLORS = [By.CSS_SELECTOR, "[for={}]"]

    # Поле "Комментарий для курьера"
    FIELD_COMMENT = [By.CSS_SELECTOR, "input[placeholder='Комментарий для курьера']"]

    # Кнопка "Заказать" под формой "Про аренду"
    BUTTON_ORDER = [By.XPATH, "//button[contains(@class, 'Button_Middle') and text()='Заказать']"]

    # кнопка "Да" в модалке "Хотите оформить заказ?"
    BUTTON_YES = [By.XPATH, "//*[contains(@class, 'Button_Middle') and text()='Да']"]

    # Заголовок "Заказ оформлен" в мод. окне
    TITLE_ORDER_MODAL = [By.CSS_SELECTOR, "[class*='Order_ModalHeader']"]

    # Кнопка "Посмотреть статус"
    BUTTON_STATUS_ORDER = [By.XPATH, "//*[text()='Посмотреть статус']"]
