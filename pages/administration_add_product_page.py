from selenium.webdriver.common.by import By

from pages.administration_products_page import AdministrationProductsPage


class AdministrationAddProductPage(AdministrationProductsPage):
    PRODUCT_NAME_INPUT = (By.CSS_SELECTOR, '#input-name-1')
    META_TAG_TITLE = (By.CSS_SELECTOR, '#input-meta-title-1')
    DATA_TAB = (By.CSS_SELECTOR, 'a[href="#tab-data"]')
    MODEL_INPUT = (By.CSS_SELECTOR, '#input-model')
    SEO_TAB = (By.CSS_SELECTOR, 'a[href="#tab-seo"]')
    SEO_KEYWORD = (By.CSS_SELECTOR, '#input-keyword-0-1')
    SAVE_BUTTON = (By.CSS_SELECTOR, 'button[title="Save"]')

    def fill_product_name(self, product_name: str):
        self.send_keys(self.PRODUCT_NAME_INPUT, product_name)

    def fill_meta_tag_title(self, tag_title: str):
        self.send_keys(self.META_TAG_TITLE, tag_title)

    def open_data_tab(self):
        self.click_on(self.DATA_TAB)

    def fill_model_name(self, model_name: str):
        self.send_keys(self.MODEL_INPUT, model_name)

    def open_seo_tab(self):
        self.click_on(self.SEO_TAB)

    def fill_seo_keyword(self, keyword: str):
        self.send_keys(self.SEO_KEYWORD, keyword)

    def click_on_save_button(self):
        self.click_on(self.SAVE_BUTTON)

    def open_products_page(self):
        self.click_on_products()
