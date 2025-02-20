import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FFOptions


def pytest_addoption(parser):
    parser.addoption('--browser', default='chrome')
    parser.addoption('--headless', action='store_true')
    parser.addoption('--url', default='http://192.168.1.135:8081',
                     help='Базовый URL страницы opencart: 192.168.1.135:8081')


@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption('--browser')
    headless = request.config.getoption('--headless')  # True - False
    url = request.config.getoption('--url')

    if browser_name in ['chrome', 'ch']:
        options = ChromeOptions()
        if headless:
            options.add_argument('--headless=new')
        driver = webdriver.Chrome(options=options)
    elif browser_name in ['firefox', 'ff']:
        options = FFOptions()
        if headless:
            options.add_argument('--headless')
        driver = webdriver.Firefox(options=options)

    driver.maximize_window()

    request.addfinalizer(driver.quit)

    driver.get(url=url)
    driver.url = url

    yield driver
