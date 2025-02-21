from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class AdministrationPage(BasePage):
    LOGOUT_BUTTON = (By.CSS_SELECTOR, '#nav-logout')
    LOGOUT_BUTTON_LABEL = (By.CSS_SELECTOR, '#nav-logout>a>span')
    CATALOG_MENU_BUTTON = (By.CSS_SELECTOR, '#menu-catalog')
    PRODUCTS_MENU_BUTTON = (By.XPATH, '//li[@id="menu-catalog"]//a[text()="Products"]')
    SUCCESS_ALERT_POPUP = (By.CSS_SELECTOR, 'div[class="alert alert-success alert-dismissible"]')
    SYSTEM_MENU_BUTTON = (By.CSS_SELECTOR, '#menu-system')
    SYSTEM_USERS_MENU_BUTTON = (By.XPATH, '//li[@id="menu-system"]//a[@href="#collapse-7-1"]')
    SYSTEM_USERS_USERS_BUTTON = (By.XPATH, '//ul[@id="collapse-7-1"]//a[text()="Users"]')

    def get_logout_button_text(self) -> str:
        return  self.get_element_text(self.LOGOUT_BUTTON_LABEL)

    def click_on_catalog(self):
        self.click_on(self.CATALOG_MENU_BUTTON)

    def click_on_products(self):
        from pages.administration_products_page import AdministrationProductsPage
        self.click_on(self.PRODUCTS_MENU_BUTTON)
        return AdministrationProductsPage(self.driver)

    def get_success_alert_popup(self):
        self.get_element(self.SUCCESS_ALERT_POPUP)

    def click_on_system(self):
        self.click_on(self.SYSTEM_MENU_BUTTON)

    def click_on_users(self):
        self.click_on(self.SYSTEM_USERS_MENU_BUTTON)

    def click_on_users_users(self):
        from pages.administration_users_page import AdministrationUsersPage
        self.click_on(self.SYSTEM_USERS_USERS_BUTTON)
        return AdministrationUsersPage(self.driver)
