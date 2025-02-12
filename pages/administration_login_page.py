from selenium.webdriver.common.by import By


class AdministrationLoginPage:
    CARD_HEADER = (By.CSS_SELECTOR, 'div.card-header')
    USERNAME_LABEL = (By.CSS_SELECTOR, 'label[for="input-username"]')
    USERNAME_INPUT = (By.CSS_SELECTOR, '#input-username')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '#input-password')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')
