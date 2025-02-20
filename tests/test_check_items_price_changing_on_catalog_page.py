from base_elements.currency_dropdown import CurrencyDropdown
from pages.catalog_page import CatalogPage


def test_check_items_price_changing_on_catalog_page(browser):
    browser.get(browser.url + '/en-gb/catalog/desktops')
    desktops_catalog_page = CatalogPage(browser)
    item_prices_in_dollars = desktops_catalog_page.get_item_prices()
    item_prices_in_dollars_texts = [str]
    for ipid in item_prices_in_dollars:
        item_prices_in_dollars_texts.append(ipid.text)
    CurrencyDropdown(browser).choose_currency(1)
    item_prices_in_pounds_sterling = desktops_catalog_page.get_item_prices()
    item_prices_in_pounds_sterling_texts = [str]
    for ipips in item_prices_in_pounds_sterling:
        item_prices_in_pounds_sterling_texts.append(ipips.text)
    assert item_prices_in_dollars_texts != item_prices_in_pounds_sterling_texts
