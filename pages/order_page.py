import allure

from data import ITEMS
from locators.locators_order_page import LocatorsOrderPage
from pages.base_page import BasePage


class OrderPage(BasePage):
    @allure.step('Кликаем по кнопке "Заказать" вверху')
    def click_order_button(self):
        self.click_with_wait(LocatorsOrderPage.ORDER_UPPER_BUTTON)

    @allure.step('Кликаем по кнопке "Заказать" посередине главной страницы')
    def click_middle_order_button(self):
        self.click_with_wait(LocatorsOrderPage.ORDER_MIDDLE_BUTTON)

    @allure.step('Находим поле Имя и помещаем туда значение')
    def set_name_input(self, name):
        name_input = self.find_element_with_wait(LocatorsOrderPage.NAME_INPUT)
        name_input.send_keys(name)

    @allure.step('Находим поле Фамилия и помещаем туда значение')
    def set_surname_input(self, surname):
        surname_input = self.find_element_with_wait(LocatorsOrderPage.SURNAME_INPUT)
        surname_input.send_keys(surname)

    @allure.step('Находим поле Адрес и помещаем туда значение')
    def set_address_input(self, address):
        address_input = self.find_element_with_wait(LocatorsOrderPage.ADDRESS_INPUT)
        address_input.send_keys(address)

    @allure.step('Кликаем по полю Метро')
    def click_metro_field(self):
        self.find_element_with_wait(LocatorsOrderPage.METRO_INPUT).click()

    @allure.step('Выбираем и кликаем по конкретной станции метро')
    def choose_metro(self, metro):
        metro_station = self.find_element_with_wait(metro)
        metro_station.click()

    @allure.step('Находим поле Телефон и помещаем туда значение')
    def set_phone_input(self, phone):
        phone_input = self.find_element_with_wait(LocatorsOrderPage.PHONE_INPUT)
        phone_input.send_keys(phone)

    @allure.step('Кликаем по кнопке Далее')
    def click_page_button_next(self):
        self.click_with_wait(LocatorsOrderPage.NEXT_BUTTON)

    @allure.step('Находим и кликаем по полю Дата заказа')
    def click_date_field(self):
        self.find_element_with_wait(LocatorsOrderPage.DATE_OF_ORDER).click()

    @allure.step('Заполняем поле дата')
    def set_date_input(self, date):
        date_input = self.find_element_with_wait(LocatorsOrderPage.DATE_OF_ORDER)
        date_input.send_keys(date)

    @allure.step('Кликаем в сторону, чтобы убрать выпадающий календарь')
    def click_header_about_rent(self):
        self.find_element_with_wait(LocatorsOrderPage.ABOUT_RENT_HEADER).click()

    @allure.step('Находим и кликаем по полю Срок аренды')
    def click_period_order(self):
        self.find_element_with_wait(LocatorsOrderPage.PERIOD_OF_ORDER).click()

    @allure.step('Выбираем срок аренды')
    def choose_period_order(self):
        self.find_element_with_wait(LocatorsOrderPage.HOW_LONG_ORDER).click()

    @allure.step('Находим поле Комментарий для курьера и вводим его')
    def set_comment_input(self, comment):
        date_input = self.find_element_with_wait(LocatorsOrderPage.COMMENT)
        date_input.send_keys(comment)

    @allure.step('Находим кнопку Заказать под формой и кликаем по ней')
    def press_button_order(self):
        self.find_element_with_wait(LocatorsOrderPage.ORDER_MIDDLE_BUTTON).click()

    @allure.step('Находим кнопку Да и кликаем по ней')
    def press_button_yes(self):
        self.find_element_with_wait(LocatorsOrderPage.BUTTON_YES).click()

    @allure.step('Нажимаем финальное "Заказать", подтверждаем действие "Да')
    def press_buttons_order_and_yes(self):
        self.press_button_order()
        self.press_button_yes()

    @allure.step('Находим заголовок "заказ оформлен"')
    def get_order_placed_text(self):
         return self.get_element_text(LocatorsOrderPage.ORDER_PLACED_TITLE)

    @allure.step('Выбираем срок аренды самоката и вставляем комментарий по желанию, набор 1')
    def click_and_choose_period_add_comment_1(self):
        self.click_period_order()
        self.choose_period_order()
        self.set_comment_input(ITEMS.COMMENT_2)

    @allure.step('Выбираем срок аренды самоката и вставляем комментарий по желанию, набор 2')
    def click_and_choose_period_add_comment_2(self):
        self.click_period_order()
        self.choose_period_order()
        self.set_comment_input(ITEMS.COMMENT_1)

    @allure.step('Заполняем поле дата заказа и убираем всплывающий календарь кликом в сторону, набор 1')
    def click_and_set_date_1(self):
        self.click_date_field()
        self.set_date_input(ITEMS.DATE_1)
        self.click_header_about_rent()

    @allure.step('Заполняем поле дата заказа и убираем всплывающий календарь кликом в сторону, набор 2')
    def click_and_set_date_2(self):
        self.click_date_field()
        self.set_date_input(ITEMS.DATE_2)
        self.click_header_about_rent()

    @allure.step('Выбираем нужную станцию метро и заполняем соответствующее поле номером телефона, набор 1')
    def choose_metro_set_phone_1(self):
        self.click_metro_field()
        self.choose_metro(LocatorsOrderPage.METRO_PREOBRAZHENKA)
        self.set_phone_input(ITEMS.PHONE_NUMBER_1)

    @allure.step('Выбираем нужную станцию метро и заполняем соответствующее поле номером телефона, набор 2')
    def choose_metro_set_phone_2(self):
        self.click_metro_field()
        self.choose_metro(LocatorsOrderPage.METRO_CHERKIZOVSKAYA)
        self.set_phone_input(ITEMS.PHONE_NUMBER_2)

    @allure.step('Заполняем поле дата заказа и убираем всплывающий календарь кликом в сторону, набор 1')
    def click_and_set_date_1(self):
        self.click_date_field()
        self.set_date_input(ITEMS.DATE_1)
        self.click_header_about_rent()

    @allure.step('Заполняем поле дата заказа и убираем всплывающий календарь кликом в сторону, набор 2')
    def click_and_set_date_2(self):
        self.click_date_field()
        self.set_date_input(ITEMS.DATE_2)
        self.click_header_about_rent()

    @allure.step('Выбираем нужную станцию метро и заполняем соответствующее поле номером телефона, набор 1')
    def choose_metro_set_phone_1(self):
        self.click_metro_field()
        self.choose_metro(LocatorsOrderPage.METRO_PREOBRAZHENKA)
        self.set_phone_input(ITEMS.PHONE_NUMBER_1)

    @allure.step('Выбираем нужную станцию метро и заполняем соответствующее поле номером телефона, набор 2')
    def choose_metro_set_phone_2(self):
        self.click_metro_field()
        self.choose_metro(LocatorsOrderPage.METRO_CHERKIZOVSKAYA)
        self.set_phone_input(ITEMS.PHONE_NUMBER_2)

    @allure.step('Передаем в соответствующие поля имя, фамилию и адрес заказа набор 1')
    def set_details_data_1(self):
        self.set_name_input(ITEMS.NAME_1)
        self.set_surname_input(ITEMS.SURNAME_1)
        self.set_address_input(ITEMS.ADDRESS_1)

    @allure.step('Передаем в соответствующие поля имя, фамилию и адрес заказа набор 2')
    def set_details_data_2(self):
        self.set_name_input(ITEMS.NAME_2)
        self.set_surname_input(ITEMS.SURNAME_2)
        self.set_address_input(ITEMS.ADDRESS_2)