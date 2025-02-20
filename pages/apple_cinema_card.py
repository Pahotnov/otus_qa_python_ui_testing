from selenium.webdriver.common.by import By


class AppleCinemaCard:
    TITLE = (By.CSS_SELECTOR, 'h1')
    PRICE = (By.CSS_SELECTOR, 'h2>span')
    AVAILABLE_OPTIONS_TITLE = (By.XPATH, './/h3[contains(text(), "Available Options")]')
    TEXT_AREA = (By.CSS_SELECTOR, '#input-option-209')
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, '#button-cart')
