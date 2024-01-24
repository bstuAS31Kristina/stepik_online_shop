from .base_page import BasePage
import selenium
from selenium import webdriver
from .locators import ProductPageLocators
class ProductPage(BasePage):
    def add_book_to_cart(self):
        button_add = self.browser.find_element(*ProductPageLocators.BUTTON_ADD)
        button_add.click()
        self.solve_quiz_and_get_code()

    def should_product_be_added_to_cart(self, book_name):
        success_msg = self.browser.find_element(*ProductPageLocators.SUCCESS_MSG)
        assert book_name == success_msg.text, "Incorrect book was added to the cart"


    def should_price_be_equal_book_price(self, book_price):
        cart_price = self.browser.find_element(*ProductPageLocators.BUSCET_MINI)
        print(book_price)
        print(cart_price.text)
        assert book_price in cart_price.text, "Price in the cart doesn't match book price"


    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MSG), "Success message is present, but should not"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MSG), ("Success message is not disappeared"
                                                                       ""
                                                                       "")
    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.BOOK_NAME).text


    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
