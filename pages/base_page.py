from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.header_locators import HeaderLocators


class Base:

    def __init__(self, driver):
        self.driver = driver

    def get_current_url(self):
        return self.driver.current_url

    def get_text_from_element(self, locator):
        element = self.find_visibility_element(locator)
        return element.text

    def find_clickable_element(self, locator):
        WebDriverWait(self.driver, 4).until(EC.element_to_be_clickable(locator))
        return self.driver.find_element(*locator)

    def find_visibility_element(self, locator):
        WebDriverWait(self.driver, 4).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def fill_input(self, locator, text: str):
        self.find_clickable_element(locator).send_keys(text)

    def scroll_to_element(self, locator):
        search_element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", search_element)

    def scroll_and_click_on_element(self, locator):
        search_element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].click();", search_element)

    def click_on_element(self, locator):
        element = self.find_clickable_element(locator)
        element.click()

    def click_button_order_on_header(self):
        self.click_on_element(HeaderLocators.ORDER_BUTTON_ON_HEADER)

    def click_logo_scooter(self):
        element = self.find_clickable_element(HeaderLocators.LOGO_SCOOTER)
        element.click()

    def click_logo_yandex(self):
        element = self.find_clickable_element(HeaderLocators.LOGO_YANDEX)
        element.click()

    # Переключиться на вкладку браузера
    def switch_to_window(self, window_index):
        open_window_list = self.driver.window_handles
        self.driver.switch_to.window(open_window_list[window_index])

    # Отформатировать локатор
    def format_locator(self, not_formatted_locator, index):
        method, locator = not_formatted_locator
        formatted_locator = locator.format(index)
        new_locator = [method, formatted_locator]
        return new_locator
