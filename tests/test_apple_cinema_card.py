from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.apple_cinema_card import AppleCinemaCard


def test_apple_cinema_card(browser):
    browser.get(browser.current_url + '/en-gb/product/desktops/apple-cinema')
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located(AppleCinemaCard.TITLE))
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located(AppleCinemaCard.PRICE))
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located(AppleCinemaCard.AVAILABLE_OPTIONS_TITLE))
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located(AppleCinemaCard.TEXT_AREA))
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located(AppleCinemaCard.ADD_TO_CART_BUTTON))
