import allure

from data import URL
from locators.locators_main_page import LocatorsMainPage
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Выбор вопроса и клик по нему')
    def get_answer_text(self, num):
        question_locator = self.format_locators(LocatorsMainPage.ACCORDION_QUESTION, num)
        answer_locator = self.format_locators(LocatorsMainPage.ACCORDION_ANSWER, num)
        self.scroll(LocatorsMainPage.QUESTION_LOCATOR_TO_SCROLL)
        self.click_with_wait(question_locator)
        return self.get_element_text(answer_locator)


    @allure.step('Ожидаем появления заголовка страницы Дзен')
    def wait_for_title_dzen(self):
        self.wait_for_title_contains('Дзен')

    @allure.step('Скрол до последнего элемента ')
    def scroll(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
