from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class AdministrationPage(BasePage):
    LOGOUT_BUTTON = (By.CSS_SELECTOR, '#nav-logout')
    LOGOUT_BUTTON_LABEL = (By.CSS_SELECTOR, '#nav-logout>a>span')

    def get_logout_button_text(self):
        return  self.get_element_text(self.LOGOUT_BUTTON_LABEL)
