from pages.main_page import MainPage


def test_add_random_item_in_cart(browser):
    cart_text = '1 item(s) - $123.20'

    main_page = MainPage(browser)
    main_page.click_on_add_to_cart_button()
    main_page.get_alert_popup()

    assert cart_text == main_page.get_cart_label_text()
