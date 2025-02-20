from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Data.data import Data
from pages.administration_login_page import AdministrationLoginPage
from pages.administration_page import AdministrationPage


def test_administration_authorization_and_deauthorization(browser):
    browser.get(browser.url + '/administration')
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located
                                    (AdministrationLoginPage.USERNAME_INPUT)).send_keys(Data.USER)
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located
                                    (AdministrationLoginPage.PASSWORD_INPUT)).send_keys(Data.PASSWORD)
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located
                                    (AdministrationLoginPage.SUBMIT_BUTTON)).click()
    logout_button_text = WebDriverWait(browser, 5).until(EC.visibility_of_element_located
                                                         (AdministrationPage.LOGOUT_BUTTON_LABEL)).text
    assert logout_button_text == 'Logout'
