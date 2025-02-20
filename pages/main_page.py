from selenium.webdriver.common.by import By


class MainPage:
    NAVIGATION = (By.CSS_SELECTOR, '#top')
    LOGO = (By.CSS_SELECTOR, '#logo')
    SEARCH = (By.CSS_SELECTOR, '#search')
    CART = (By.CSS_SELECTOR, '#header-cart')
    CONTAINER = (By.CSS_SELECTOR, '#common-home')
    ALERT_POPUP = (By.CSS_SELECTOR, 'div[class="alert alert-success alert-dismissible"]')
    ADD_TO_CART_BUTTON = (By.XPATH, '(.//button[contains(@formaction, "http://192.168.1.135:8081/en-gb?route=checkout/cart.add")])[2]')
    CART_LABEL = (By.CSS_SELECTOR, '#header-cart>div>button')
    CURRENCY_DROPDOWN = (By.CSS_SELECTOR, '#form-currency')
    ITEMS_PRICES = (By.CSS_SELECTOR, 'span[class*="price"]')
    CURRENCY_DROPDOWN_ITEMS = (By.CSS_SELECTOR, '#form-currency>div>ul>li>a')
