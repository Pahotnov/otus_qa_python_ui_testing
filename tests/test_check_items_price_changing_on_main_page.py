from base_elements.currency_dropdown import CurrencyDropdown
from pages.main_page import MainPage


def test_check_items_price_changing_on_main_page(browser):
    main_page = MainPage(browser)
    item_prices_in_dollars = main_page.get_item_prices()
    item_prices_in_dollars_texts = [str]
    for ipid in item_prices_in_dollars:
        item_prices_in_dollars_texts.append(ipid.text)
    CurrencyDropdown(browser).choose_currency(0)
    item_prices_in_euros = main_page.get_item_prices()
    item_prices_in_euros_texts = [str]
    for ipie in item_prices_in_euros:
        item_prices_in_euros_texts.append(ipie.text)
    assert item_prices_in_dollars_texts != item_prices_in_euros_texts
