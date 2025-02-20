from Data.data import Data
from pages.administration_login_page import AdministrationLoginPage


def test_administration_authorization_and_deauthorization(browser):
    browser.get(browser.url + '/administration')
    administration_login_page = AdministrationLoginPage(browser)
    administration_login_page.fill_username_field(Data.USER)
    administration_login_page.fill_password_field(Data.PASSWORD)
    administration_page = administration_login_page.click_on_submit_button()
    assert administration_page.get_logout_button_text() == 'Logout'
