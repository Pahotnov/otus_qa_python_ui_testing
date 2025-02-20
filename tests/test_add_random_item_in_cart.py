from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.main_page import MainPage


def test_add_random_item_in_cart(browser):
    browser.get(browser.url)
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located(MainPage.ADD_TO_CART_BUTTON)).click()
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located(MainPage.ALERT_POPUP))
    cart_text = WebDriverWait(browser, 5).until(EC.visibility_of_element_located(MainPage.CART_LABEL)).text
    assert '1 item(s) - $123.20' == cart_text
