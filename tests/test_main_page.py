from pages.main_page import MainPage


def test_main_page(browser):
    main_page = MainPage(browser)
    main_page.get_navigation()
    main_page.get_logo()
    main_page.get_search()
    main_page.get_cart()
    main_page.get_container()
