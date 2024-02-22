from selenium.webdriver.common.by import By


class HomePageLocators:
    # Кнопка "Заказать" на странице
    ORDER_BUTTON_ON_PAGE = [By.CSS_SELECTOR, "button[class*='Button_Middle']"]

    # Заголовок страницы "Самокат на пару дней"
    HOME_TITLE = [By.CLASS_NAME, "Home_Header__iJKdX"]

    # Заголовок списка "Вопросы о важном"
    TITLE_ACCORDION = [By.XPATH, "//*[text()='Вопросы о важном']"]

    # Локатор всех вопросов
    QUESTIONS = [By.ID, "accordion__heading-{}"]

    # Локатор всех ответов
    ANSWERS = [By.CSS_SELECTOR, "[id='accordion__panel-{}']>p"]
