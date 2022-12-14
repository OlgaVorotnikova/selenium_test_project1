from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket_button.click()

    def should_be_message_about_adding_product_to_basket(self):
        product_localor = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        message = self.browser.find_element(*ProductPageLocators.MESSAGE_SUCCESS_PRODUCT)
        assert product_localor.text == message.text, f"Message about adding the product is not correct: {message.text}"

    def should_be_message_about_basket_value(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        message = self.browser.find_element(*ProductPageLocators.MESSAGE_SUCCESS_BASKET)
        assert product_price.text == message.text, f"Message about product price is not correct: {message.text}"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def success_message_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"