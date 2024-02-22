from selenium.webdriver.common.by import By


class HeaderLocators:
    # Логотип "Самокат"
    LOGO_SCOOTER = [By.CSS_SELECTOR, "[alt='Scooter']"]

    # Логотип "Яндекс"
    LOGO_YANDEX = [By.CSS_SELECTOR, "[alt='Yandex']"]

    # Кнопка "Заказать"
    ORDER_BUTTON_ON_HEADER = [By.XPATH, "//*[contains(@class, 'Button_Button') and text()='Заказать']"]
