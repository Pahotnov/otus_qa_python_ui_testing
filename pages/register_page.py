from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class RegisterPage(BasePage):
    TITLE = (By.CSS_SELECTOR, 'h1')
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, '#input-firstname')
    LAST_NAME_INPUT = (By.CSS_SELECTOR, '#input-lastname')
    EMAIL_INPUT = (By.CSS_SELECTOR, '#input-email')
    REGISTER_COLUMN = (By.CSS_SELECTOR, '#column-right')

    def get_title(self):
        self.get_element(self.TITLE)

    def get_first_name_input(self):
        self.get_element(self.FIRST_NAME_INPUT)

    def get_last_name_input(self):
        self.get_element(self.LAST_NAME_INPUT)

    def get_email_input(self):
        self.get_element(self.EMAIL_INPUT)

    def get_register_column(self):
        self.get_element(self.REGISTER_COLUMN)
