from pages.catalog_page import CatalogPage


def test_catalog(browser):
    browser.get(browser.current_url + '/en-gb/catalog/desktops')
    desktops_catalog_page = CatalogPage(browser)
    desktops_catalog_page.get_title()
    desktops_catalog_page.get_catalog_image()
    desktops_catalog_page.get_refine_search()
    desktops_catalog_page.get_product_compare_option()
    desktops_catalog_page.get_product_list()
