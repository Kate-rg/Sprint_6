import pytest
from selenium import webdriver
from data import CookieLocator
from urls import URL


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Firefox()
    driver.set_window_size(1536, 864)
    driver.get(URL.FIRST_PAGE)

    driver.find_element(*CookieLocator.COOKIE_BUTTON).click()

    yield driver

    driver.quit()