from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.register_page import RegisterPage


def test_register_page(browser):
    browser.get(browser.url + '/en-gb?route=account/register')
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located(RegisterPage.TITLE))
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located(RegisterPage.REGISTER_COLUMN))
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located(RegisterPage.FIRST_NAME_INPUT))
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located(RegisterPage.LAST_NAME_INPUT))
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located(RegisterPage.EMAIL_INPUT))
