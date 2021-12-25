from pages.base import BasePage
from pages.cart import CartPage


class CheckoutPage(BasePage):

    def __init__(self, driver, username, password):
        self.__cart_page = CartPage(driver, username, password)
        self.__cart_page.checkout()
        super().__init__(self.__cart_page.driver, self.__cart_page.driver.current_url)

    def click_cancel(self):
        cancel_button = self.find_element_if_present('id', 'cancel')
        cancel_button.click()

    def click_continue(self):
        if self.driver.current_url == 'https://www.saucedemo.com/checkout-step-one.html':
            continue_button = self.find_element_if_present('id', 'continue')
            continue_button.click()
        else:
            raise Exception()

    def click_finish(self):
        if self.driver.current_url == 'https://www.saucedemo.com/checkout-step-two.html':
            finish_button = self.find_element_if_present('id', 'finish')
            finish_button.click()
        else:
            raise Exception()

    def click_back_home(self):
        if self.driver.current_url == 'https://www.saucedemo.com/checkout-complete.html':
            back_home_button = self.find_element_if_present('id', 'back-to-products')
            back_home_button.click()
        else:
            raise Exception()

    def enter_first_name(self, first_name):
        if self.driver.current_url == 'https://www.saucedemo.com/checkout-step-one.html':
            first_name_input = self.find_element_if_present('id', 'first-name')
            first_name_input.send_keys(first_name)
        else:
            raise Exception()

    def enter_last_name(self, last_name):
        if self.driver.current_url == 'https://www.saucedemo.com/checkout-step-one.html':
            last_name_input = self.find_element_if_present('id', 'last-name')
            last_name_input.send_keys(last_name)
        else:
            raise Exception()

    def enter_postal_code(self, postal_code):
        if self.driver.current_url == 'https://www.saucedemo.com/checkout-step-one.html':
            postal_code_input = self.find_element_if_present('id', 'postal-code')
            postal_code_input.send_keys(postal_code)
        else:
            raise Exception()

    def read_error_message(self):
        if self.driver.current_url == 'https://www.saucedemo.com/checkout-step-one.html':
            error_message = self.find_element_if_present('tag_name', 'h3').text
            return error_message
        else:
            raise Exception()
