from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.catalog_page import CatalogPage


def test_catalog(browser):
    browser.get(browser.current_url + '/en-gb/catalog/desktops')
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located(CatalogPage.TITLE))
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located(CatalogPage.CATALOG_IMAGE))
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located(CatalogPage.REFINE_SEARCH))
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located(CatalogPage.PRODUCT_COMPARE_OPTION))
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located(CatalogPage.PRODUCT_LIST))
