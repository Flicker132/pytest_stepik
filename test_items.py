import time


def test_guest_should_see_add_to_basket_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30)

    add_to_basket_button = browser.find_elements_by_css_selector("button.btn-add-to-basket")

    assert len(add_to_basket_button) > 0, "Add to basket button is not found on the page"

    assert add_to_basket_button[0].is_displayed(), "Add to basket button is not visible"
