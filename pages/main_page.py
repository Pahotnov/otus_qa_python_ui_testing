from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class MainPage(BasePage):
    NAVIGATION = (By.CSS_SELECTOR, '#top')
    LOGO = (By.CSS_SELECTOR, '#logo')
    SEARCH = (By.CSS_SELECTOR, '#search')
    CART = (By.CSS_SELECTOR, '#header-cart')
    CONTAINER = (By.CSS_SELECTOR, '#common-home')
    ALERT_POPUP = (By.CSS_SELECTOR, 'div[class="alert alert-success alert-dismissible"]')
    ADD_TO_CART_BUTTON = (By.XPATH, '(.//button[contains(@formaction, "http://192.168.1.135:8081/en-gb?route=checkout/cart.add")])[2]')
    CART_LABEL = (By.CSS_SELECTOR, '#header-cart>div>button')
    CURRENCY_DROPDOWN = (By.CSS_SELECTOR, '#form-currency')
    ITEMS_PRICES = (By.CSS_SELECTOR, 'span[class*="price"]')

    def get_navigation(self):
        self.get_element(self.NAVIGATION)

    def get_logo(self):
        self.get_element(self.LOGO)

    def get_search(self):
        self.get_element(self.SEARCH)

    def get_cart(self):
        self.get_element(self.CART)

    def get_container(self):
        self.get_element(self.CONTAINER)

    def click_on_add_to_cart_button(self):
        self.click_on(self.ADD_TO_CART_BUTTON)

    def get_alert_popup(self):
        self.get_element(self.ALERT_POPUP)

    def get_cart_label_text(self):
        return self.get_element_text(self.CART_LABEL)

    def get_item_prices(self):
       return  self.get_elements(self.ITEMS_PRICES)
