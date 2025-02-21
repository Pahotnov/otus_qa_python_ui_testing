from selenium.webdriver.common.by import By

from pages.administration_page import AdministrationPage


class AdministrationProductsPage(AdministrationPage):
    ADD_BUTTON = (By.CSS_SELECTOR, 'div.float-end > a[href*="http://192.168.1.135:8081/'
                                   'administration/index.php?route=catalog/product.form&user_token"]')
    FILTER_PRODUCT_NAME = (By.CSS_SELECTOR, '#input-name')
    FILTER_APPLY_BUTTON = (By.CSS_SELECTOR, '#button-filter')
    CHOOSE_ALL_CHECKBOX = (By.XPATH, '(//input[@class="form-check-input"])[1]')
    DELETE_BUTTON = (By.CSS_SELECTOR, 'button[title="Delete"]')

    def click_on_add_button(self):
        from pages.administration_add_product_page import AdministrationAddProductPage
        self.click_on(self.ADD_BUTTON)
        return AdministrationAddProductPage(self.driver)

    def fill_filter_product_name(self, product_name: str):
        self.send_keys(self.FILTER_PRODUCT_NAME, product_name)

    def click_on_filter_apply_button(self):
        self.click_on(self.FILTER_APPLY_BUTTON)

    def click_on_choose_all_products_checkbox(self):
        self.click_on(self.CHOOSE_ALL_CHECKBOX)

    def click_on_delete_button(self):
        self.click_on(self.DELETE_BUTTON)
