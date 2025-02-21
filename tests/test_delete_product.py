from random import randint

from Data.data import Data
from pages.administration_login_page import AdministrationLoginPage


def test_delete_product(browser):
    product_name = 'test'
    meta_tag_title = 'TEST'
    model_name = 'test_model'
    seo_keyword = str(randint(1, 9999999999))

    browser.get(f'{browser.url}/administration')
    administration_login_page = AdministrationLoginPage(browser)
    administration_login_page.fill_username_field(Data.USER)
    administration_login_page.fill_password_field(Data.PASSWORD)
    administration_page = administration_login_page.click_on_submit_button()
    administration_page.click_on_catalog()
    administration_products_page = administration_page.click_on_products()
    administration_add_product_page = administration_products_page.click_on_add_button()
    administration_add_product_page.fill_product_name(product_name)
    administration_add_product_page.fill_meta_tag_title(meta_tag_title)
    administration_add_product_page.open_data_tab()
    administration_add_product_page.fill_model_name(model_name)
    administration_add_product_page.open_seo_tab()
    administration_add_product_page.fill_seo_keyword(seo_keyword)
    administration_add_product_page.click_on_save_button()
    administration_add_product_page.get_success_alert_popup()
    administration_products_page = administration_add_product_page.click_on_products()
    administration_products_page.fill_filter_product_name(product_name)
    administration_products_page.click_on_filter_apply_button()
    administration_products_page.click_on_choose_all_products_checkbox()
    administration_products_page.click_on_delete_button()
    alert = browser.switch_to.alert
    alert.accept()
    administration_products_page.get_success_alert_popup()
