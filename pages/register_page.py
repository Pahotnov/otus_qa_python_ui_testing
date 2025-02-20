from selenium.webdriver.common.by import By


class RegisterPage:
    TITLE = (By.CSS_SELECTOR, 'h1')
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, '#input-firstname')
    LAST_NAME_INPUT = (By.CSS_SELECTOR, '#input-lastname')
    EMAIL_INPUT = (By.CSS_SELECTOR, '#input-email')
    REGISTER_COLUMN = (By.CSS_SELECTOR, '#column-right')
