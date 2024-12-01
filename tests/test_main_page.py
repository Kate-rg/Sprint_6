from pages.main_page import MainPage
import pytest
import allure

from data import Questions


class TestQuestionsPage:

    @allure.title('Проверка ответов соответствующим открываемым вопросам')
    @allure.description('Через метод параметризации поочередно проверяем соответствие текста ответов вопросам')
    @pytest.mark.parametrize('question', Questions.ANSWERS)
    def test_click_and_get_answer(self, driver, question):
        number, correct_answer = question
        question_page = MainPage(driver)
        answer = question_page.get_answer_text(number)

        assert answer == correct_answer

