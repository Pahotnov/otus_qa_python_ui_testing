from pages.administration_login_page import AdministrationLoginPage


def test_administration_login_page(browser):
    browser.get(browser.url + '/administration')
    administration_login_page = AdministrationLoginPage(browser)
    administration_login_page.get_card_header()
    administration_login_page.get_username_label()
    administration_login_page.get_username_input()
    administration_login_page.get_password_input()
    administration_login_page.get_submit_button()
