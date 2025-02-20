from locale import currency

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class CurrencyDropdown:
    CURRENCY_DROPDOWN = (By.CSS_SELECTOR, '#form-currency')
    CURRENCY_DROPDOWN_ITEMS = (By.XPATH, '//ul[@class="dropdown-menu show"]/li/a')

    def __init__(self, browser):
        self.driver = browser

    def choose_currency(self, index: int):
        (WebDriverWait(self.driver, 10).until
         (expected_conditions.visibility_of_element_located(self.CURRENCY_DROPDOWN))).click()
        (WebDriverWait(self.driver, 10).until
         (expected_conditions.visibility_of_all_elements_located(self.CURRENCY_DROPDOWN_ITEMS)))[index].click()
