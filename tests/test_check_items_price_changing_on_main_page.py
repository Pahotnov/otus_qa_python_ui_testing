from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.main_page import MainPage


def test_check_items_price_changing_on_main_page(browser):
    browser.get(browser.url)
    item_prices_in_dollars = WebDriverWait(browser, 5).until(EC.visibility_of_all_elements_located(MainPage.ITEMS_PRICES))
    item_prices_in_dollars_texts = [str]
    for ipid in item_prices_in_dollars:
        item_prices_in_dollars_texts.append(ipid.text)
    browser.find_element(*MainPage.CURRENCY_DROPDOWN).click()
    currencies = browser.find_elements(*MainPage.CURRENCY_DROPDOWN_ITEMS)
    currencies[0].click()
    item_prices_in_euros = WebDriverWait(browser, 5).until(EC.visibility_of_all_elements_located(MainPage.ITEMS_PRICES))
    item_prices_in_euros_texts = [str]
    for ipie in item_prices_in_euros:
        item_prices_in_euros_texts.append(ipie.text)
    assert item_prices_in_dollars_texts != item_prices_in_euros_texts
