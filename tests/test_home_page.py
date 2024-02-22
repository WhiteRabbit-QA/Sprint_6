import allure
import pytest
from data import Answers
from locators.home_page_locators import HomePageLocators
from pages.home_page import HomePage


class TestHomePage:

    @allure.title('Проверка получения ответов по каждому вопросу в выпадающем списке')
    @allure.description('В разделе "Вопросы о важном" кликаем на каждый вопрос и проверяем текст ответа')
    @pytest.mark.parametrize(
        'n, expected_result',
        [
            pytest.param(*(0, Answers.answer_text[0]), id="First_question"),
            pytest.param(*(1, Answers.answer_text[1]), id="Second_question"),
            pytest.param(*(2, Answers.answer_text[2]), id="Third_question"),
            pytest.param(*(3, Answers.answer_text[3]), id="Fourth_question"),
            pytest.param(*(4, Answers.answer_text[4]), id="Fifth_question"),
            pytest.param(*(5, Answers.answer_text[5]), id="Sixth_question"),
            pytest.param(*(6, Answers.answer_text[6]), id="Seventh_question"),
            pytest.param(*(7, Answers.answer_text[7]), id="Eighth_question")
        ])
    def test_correct_answers_for_questions(self, driver, click_cookies_button, n, expected_result):
        home = HomePage(driver)
        with allure.step('Скролл страницы до раздела "Вопросы о важном"'):
            home.scroll_to_element(HomePageLocators.TITLE_ACCORDION)
        with allure.step('Кликнуть на вопрос и считать текст ответа'):
            text = home.get_text_answer_for_ich_question(HomePageLocators.QUESTIONS, HomePageLocators.ANSWERS, n)
        assert text == expected_result
