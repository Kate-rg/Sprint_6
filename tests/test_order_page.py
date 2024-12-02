import allure

from pages.order_page import OrderPage


class TestOrderPage:
    @allure.title('Заполнение формы заказа самоката с набором данных №1')
    @allure.description('Заполняем форму заказа самоката из двух частей и убеждаемся в положительном финальном итоге заполнения')
    def test_order_page_scenario_1(self, driver):
        order_page = OrderPage(driver)
        order_page.click_order_button()
        order_page.set_details_data_1()
        order_page.choose_metro_set_phone_1()
        order_page.click_page_button_next()
        order_page.click_and_set_date_1()
        order_page.click_and_choose_period_add_comment_1()
        order_page.press_buttons_order_and_yes()

        assert 'Заказ оформлен' in order_page.get_order_placed_text()

    @allure.title('Заполнение формы заказа самоката с набором данных №2')
    @allure.description('Заполняем форму заказа самоката из двух частей и убеждаемся в положительном финальном итоге заполнения')
    def test_order_page_scenario_2(self, driver):
        order_page = OrderPage(driver)
        order_page.click_middle_order_button()
        order_page.set_details_data_2()
        order_page.choose_metro_set_phone_2()
        order_page.click_page_button_next()
        order_page.click_and_set_date_2()
        order_page.click_and_choose_period_add_comment_2()
        order_page.press_buttons_order_and_yes()

        assert 'Заказ оформлен' in order_page.get_order_placed_text()






