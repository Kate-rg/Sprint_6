import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ищим элемент с ожижанием')
    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Клик на кнопку')
    def click_with_wait(self, locator):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(locator))
        button=self.driver.find_element(*locator)
        button.click()

    def get_element_text(self, locator):
        return self.find_element_with_wait(locator).text


    def format_locators(self, locator_1, num):
        method, locator = locator_1
        locator=locator.format(num)
        return method, locator

    @allure.step('Ожидание загрузки новой страницы')
    def wait_url_changes(self, url):
        WebDriverWait(self.driver, 3).until(expected_conditions.url_changes(url))

    @allure.step('Ожидаем появления заголовка страницы Дзен')
    def wait_for_title(self):
        self.wait_for_title_contains('Дзен')

    @allure.step('Переход на последнюю вкладку')
    def switch_driver(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step('Ожидание нужного заголовка')
    def wait_for_title_contains(self, title):
        WebDriverWait(self.driver, 3).until(expected_conditions.title_contains(title))