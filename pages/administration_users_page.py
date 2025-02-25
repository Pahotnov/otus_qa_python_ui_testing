from selenium.webdriver.common.by import By

from pages.administration_page import AdministrationPage


class AdministrationUsersPage(AdministrationPage):
    ADD_BUTTON = (By.CSS_SELECTOR, 'div.float-end > a[href*="http://192.168.1.135:8081/'
                                   'administration/index.php?route=user/user.form&user_token"]')

    def click_on_add_button(self):
        from pages.administration_add_user_page import AdministrationAddUserPage
        self.click_on(self.ADD_BUTTON)
        return AdministrationAddUserPage(self.driver)
