from selenium.webdriver.common.by import By

from pages.administration_page import AdministrationPage


class AdministrationAddUserPage(AdministrationPage):
    USERNAME = (By.CSS_SELECTOR, '#input-username')
    FIRST_NAME = (By.CSS_SELECTOR, '#input-firstname')
    LAST_NAME = (By.CSS_SELECTOR, '#input-lastname')
    EMAIL = (By.CSS_SELECTOR, '#input-email')
    PASSWORD = (By.CSS_SELECTOR, '#input-password')
    CONFIRM = (By.CSS_SELECTOR, '#input-confirm')
    SAVE_BUTTON = (By.CSS_SELECTOR, 'div.float-end > button[title="Save"]')

    def fill_username(self, username: str):
        self.send_keys(self.USERNAME, username)

    def fill_first_name(self, first_name: str):
        self.send_keys(self.FIRST_NAME, first_name)

    def fill_last_name(self, last_name: str):
        self.send_keys(self.LAST_NAME, last_name)

    def fill_email(self, email: str):
        self.send_keys(self.EMAIL, email)

    def fill_password(self, password: str):
        self.send_keys(self.PASSWORD, password)

    def fill_confirm(self, confirm: str):
        self.send_keys(self.CONFIRM, confirm)

    def click_on_save_button(self):
        self.click_on(self.SAVE_BUTTON)
