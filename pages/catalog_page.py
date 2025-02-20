from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CatalogPage(BasePage):
    TITLE = (By.CSS_SELECTOR, 'h2')
    CATALOG_IMAGE = (By.CSS_SELECTOR, 'img[title="Desktops"]')
    REFINE_SEARCH = (By.CSS_SELECTOR, 'h3')
    PRODUCT_COMPARE_OPTION = (By.CSS_SELECTOR, '#compare-total')
    PRODUCT_LIST = (By.CSS_SELECTOR, '#product-list')
    ITEMS_PRICES = (By.CSS_SELECTOR, 'span[class*="price"]')

    def get_title(self):
        self.get_element(self.TITLE)

    def get_catalog_image(self):
        self.get_element(self.CATALOG_IMAGE)

    def get_refine_search(self):
        self.get_element(self.REFINE_SEARCH)

    def get_product_compare_option(self):
        self.get_element(self.PRODUCT_COMPARE_OPTION)

    def get_product_list(self):
        self.get_element(self.PRODUCT_LIST)

    def get_item_prices(self):
        return self.get_elements(self.ITEMS_PRICES)
