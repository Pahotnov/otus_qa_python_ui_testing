from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class AppleCinemaCard(BasePage):
    TITLE = (By.CSS_SELECTOR, 'h1')
    PRICE = (By.CSS_SELECTOR, 'h2>span')
    AVAILABLE_OPTIONS_TITLE = (By.XPATH, './/h3[contains(text(), "Available Options")]')
    TEXT_AREA = (By.CSS_SELECTOR, '#input-option-209')
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, '#button-cart')

    def get_title(self):
        self.get_element(self.TITLE)

    def get_price(self):
        self.get_element(self.PRICE)

    def get_available_options_title(self):
        self.get_element(self.AVAILABLE_OPTIONS_TITLE)

    def get_text_area(self):
        self.get_element(self.TEXT_AREA)

    def get_add_to_cart_button(self):
        self.get_element(self.ADD_TO_CART_BUTTON)
