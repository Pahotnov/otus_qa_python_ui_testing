from pages.apple_cinema_card import AppleCinemaCard


def test_apple_cinema_card(browser):
    browser.get(browser.url + '/en-gb/product/desktops/apple-cinema')
    apple_cinema_card_page = AppleCinemaCard(browser)
    apple_cinema_card_page.get_title()
    apple_cinema_card_page.get_price()
    apple_cinema_card_page.get_available_options_title()
    apple_cinema_card_page.get_text_area()
    apple_cinema_card_page.get_add_to_cart_button()
