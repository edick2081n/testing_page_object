from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_PRODUCT)
        button.click()

    def should_be_message1(self):
        name_product_element = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT)
        name_product = name_product_element.text
        name_product_basket_element = self.browser.find_element(*ProductPageLocators.MESSAGE_NAME_PRODUCT)
        name_product_basket = name_product_basket_element.text
        assert name_product==name_product_basket, "the product is not added"

    def should_be_message2(self):
        product_price_element = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        product_price = product_price_element.text
        amount_basket_element = self.browser.find_element(*ProductPageLocators.CURRENT_AMOUNT_BASKET)
        amount_basket = amount_basket_element.text
        assert product_price==amount_basket, f"the {amount_basket} not equal {product_price}"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"




