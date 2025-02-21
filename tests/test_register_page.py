from pages.register_page import RegisterPage


def test_register_page(browser):
    browser.get(browser.url + '/en-gb?route=account/register')
    register_page = RegisterPage(browser)
    register_page.get_title()
    register_page.get_register_column()
    register_page.get_first_name_input()
    register_page.get_last_name_input()
    register_page.get_email_input()
