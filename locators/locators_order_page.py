from selenium.webdriver.common.by import By

class LocatorsOrderPage:
    ORDER_UPPER_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g']")
    ORDER_MIDDLE_BUTTON = By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM'and text()='Заказать']"
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")
    ORDER_PLACED_TITLE = (By.XPATH, "//*[@class='Order_ModalHeader__3FDaJ']")
    BUTTON_YES = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Да']")
    NAME_INPUT = (By.CSS_SELECTOR, "[placeholder='* Имя']")
    SURNAME_INPUT = (By.CSS_SELECTOR, "[placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.CSS_SELECTOR, "[placeholder='* Адрес: куда привезти заказ']")
    METRO_INPUT = (By.XPATH, "//input[@class='select-search__input']")
    METRO_CHERKIZOVSKAYA = (By.XPATH, "//button[@value='2']")
    METRO_PREOBRAZHENKA = (By.XPATH, "//button[@value='3']")
    PHONE_INPUT = (By.CSS_SELECTOR, "[placeholder='* Телефон: на него позвонит курьер']")
    ABOUT_RENT_HEADER = (By.XPATH, "//div[@class='Order_Header__BZXOb']")
    DATE_OF_ORDER = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    PERIOD_OF_ORDER = (By.CSS_SELECTOR, ".Dropdown-placeholder")
    HOW_LONG_ORDER = (By.XPATH, "//div[@class='Dropdown-option' and text()='сутки']")
    COMMENT = (By.CSS_SELECTOR, "[placeholder='Комментарий для курьера']")
