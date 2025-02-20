from selenium.webdriver.common.by import By

from pages.administration_page import AdministrationPage
from pages.base_page import BasePage


class AdministrationLoginPage(BasePage):
    CARD_HEADER = (By.CSS_SELECTOR, 'div.card-header')
    USERNAME_LABEL = (By.CSS_SELECTOR, 'label[for="input-username"]')
    USERNAME_INPUT = (By.CSS_SELECTOR, '#input-username')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '#input-password')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')

    def get_card_header(self):
        self.get_element(self.CARD_HEADER)

    def get_username_label(self):
        self.get_element(self.USERNAME_LABEL)

    def get_username_input(self):
        self.get_element(self.USERNAME_INPUT)

    def get_password_input(self):
        self.get_element(self.PASSWORD_INPUT)

    def get_submit_button(self):
        self.get_element(self.SUBMIT_BUTTON)

    def fill_username_field(self, username: str):
        self.send_keys(self.USERNAME_INPUT, username)

    def fill_password_field(self, password: str):
        self.send_keys(self.PASSWORD_INPUT, password)

    def click_on_submit_button(self):
        self.click_on(self.SUBMIT_BUTTON)
        return AdministrationPage(self.driver)

