from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from conftest import browser


class BasePage:
    def __init__(self, browser):
        self.driver = browser

    def get_element(self, locator) -> WebElement:
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(locator))

    def get_elements(self, locator) -> list[WebElement]:
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_all_elements_located(locator))

    def click_on(self, locator):
        self.get_element(locator).click()

    def get_element_text(self, locator) -> str:
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(locator)).text

    def send_keys(self, locator, data):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(locator)).send_keys(data)
