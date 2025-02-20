from selenium.webdriver.common.by import By


class AdministrationPage:
    LOGOUT_BUTTON = (By.CSS_SELECTOR, '#nav-logout')
    LOGOUT_BUTTON_LABEL = (By.CSS_SELECTOR, '#nav-logout>a>span')
