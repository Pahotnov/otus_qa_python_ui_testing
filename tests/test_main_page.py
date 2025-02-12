from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.main_page import MainPage


def test_main_page(browser):
    browser.get(browser.current_url)
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located(MainPage.NAVIGATION))
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located(MainPage.LOGO))
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located(MainPage.SEARCH))
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located(MainPage.CART))
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located(MainPage.CONTAINER))
