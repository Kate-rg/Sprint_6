from selenium.webdriver.common.by import By


class LocatorsMainPage:

    ACCORDION_QUESTION = By.XPATH, "//*[@id='accordion__heading-{}']"

    ACCORDION_ANSWER = By.XPATH, "//*[@id='accordion__panel-{}']"

    QUESTION_LOCATOR_TO_SCROLL = By.XPATH, "//*[@id='accordion__heading-7']"