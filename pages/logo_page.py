import allure

from locators.locators_logo_page import LocatorsLogoPage
from pages.base_page import BasePage
from urls import URL


class LogoPage(BasePage):
    @allure.step('Кликаем по кнопке "Заказать" вверху')
    def click_order_button(self):
        self.click_with_wait(LocatorsLogoPage.ORDER_UPPER_BUTTON)

    @allure.step('Кликаем по лого Самоката')
    def click_logo_scooter(self):
        self.click_with_wait(LocatorsLogoPage.SAMOKAT_BUTTON)

    @allure.step('Кликаем по лого Яндекса')
    def click_logo_yandex(self):
        self.click_with_wait(LocatorsLogoPage.YANDEX_BUTTON)

    @allure.step('Ожидаем пока изменится страница на Дзен')
    def wait_for_url_changes_to_dzen(self):
        self.wait_url_changes(URL.DZEN_PAGE)

    def get_current_url(self):
        return self.driver.current_url
