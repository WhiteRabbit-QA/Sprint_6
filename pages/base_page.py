import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открыть страницу')
    def open_page(self, url):
        self.driver.get(url)

    @allure.step('Получить текущий url')
    def get_url(self):
        return self.driver.current_url

    @allure.step('Получить текст элемента')
    def get_text_from_element(self, locator):
        element = self.find_visibility_element(locator)
        return element.text

    @allure.step('Найти кликабельный элемент')
    def find_clickable_element(self, locator):
        WebDriverWait(self.driver, 4).until(EC.element_to_be_clickable(locator))
        return self.driver.find_element(*locator)

    @allure.step('Найти видимый элемент')
    def find_visibility_element(self, locator):
        WebDriverWait(self.driver, 4).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Заполнить поле')
    def fill_input(self, locator, text: str):
        self.find_clickable_element(locator).send_keys(text)

    @allure.step('Скролл до элемента')
    def scroll_to_element(self, locator):
        search_element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", search_element)

    @allure.step('Проскроллить до элемента и нажать на него')
    def scroll_and_click_on_element(self, locator):
        search_element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].click();", search_element)

    @allure.step('Нажать на элемент')
    def click_on_element(self, locator):
        element = self.find_clickable_element(locator)
        element.click()

    @allure.step('Переключиться на вкладку браузера')
    def switch_to_window(self, window_index):
        open_window_list = self.driver.window_handles
        self.driver.switch_to.window(open_window_list[window_index])

    @allure.step('Отформатировать локатор')
    def format_locator(self, not_formatted_locator, index):
        method, locator = not_formatted_locator
        formatted_locator = locator.format(index)
        new_locator = [method, formatted_locator]
        return new_locator
