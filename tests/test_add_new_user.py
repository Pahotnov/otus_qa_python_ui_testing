from Data import data_helper
from Data.data import Data
from pages.administration_login_page import AdministrationLoginPage


def test_add_new_user(browser):
    username = data_helper.get_random_username(10)
    first_name = data_helper.get_random_username(8)
    last_name = data_helper.get_random_username(14)
    e_mail = f'{data_helper.get_random_string(12)}@mail.com'
    password = data_helper.get_random_string(10)

    browser.get(f'{browser.url}/administration')
    administration_login_page = AdministrationLoginPage(browser)
    administration_login_page.fill_username_field(Data.USER)
    administration_login_page.fill_password_field(Data.PASSWORD)
    administration_page = administration_login_page.click_on_submit_button()
    administration_page.click_on_system()
    administration_page.click_on_users()
    administration_users_page = administration_page.click_on_users_users()
    administration_add_user_page = administration_users_page.click_on_add_button()
    administration_add_user_page.fill_username(username)
    administration_add_user_page.fill_first_name(first_name)
    administration_add_user_page.fill_last_name(last_name)
    administration_add_user_page.fill_email(e_mail)
    administration_add_user_page.fill_password(password)
    administration_add_user_page.fill_confirm(password)
    administration_add_user_page.click_on_save_button()
    administration_add_user_page.get_success_alert_popup()
