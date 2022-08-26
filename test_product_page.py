from .pages.product_page import ProductPage
import time

actual_link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"

def test_guest_can_add_product_to_basket(browser):
    link = actual_link
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.solve_quiz_and_get_code()
#    time.sleep(500)
    product_page.should_be_message_about_adding_product_to_basket()
    product_page.should_be_message_about_basket_value()