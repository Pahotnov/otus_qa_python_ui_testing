from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.administration_login_page import AdministrationLoginPage


def test_administration_login_page(browser):
    browser.get(browser.url + '/administration')
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located(AdministrationLoginPage.CARD_HEADER))
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located(AdministrationLoginPage.USERNAME_LABEL))
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located(AdministrationLoginPage.USERNAME_INPUT))
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located(AdministrationLoginPage.PASSWORD_INPUT))
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located(AdministrationLoginPage.SUBMIT_BUTTON))
