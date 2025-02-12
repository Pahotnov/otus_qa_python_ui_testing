from selenium.webdriver.common.by import By


class CatalogPage:
    TITLE = (By.CSS_SELECTOR, 'h2')
    CATALOG_IMAGE = (By.CSS_SELECTOR, 'img[title="Desktops"]')
    REFINE_SEARCH = (By.CSS_SELECTOR, 'h3')
    PRODUCT_COMPARE_OPTION = (By.CSS_SELECTOR, '#compare-total')
    PRODUCT_LIST = (By.CSS_SELECTOR, '#product-list')
    CURRENCY_DROPDOWN = (By.CSS_SELECTOR, '#form-currency')
    ITEMS_PRICES = (By.CSS_SELECTOR, 'span[class*="price"]')
    CURRENCY_DROPDOWN_ITEMS = (By.CSS_SELECTOR, '#form-currency>div>ul>li>a')
