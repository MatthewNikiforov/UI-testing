import pytest
from pages.checkout import CheckoutPage


@pytest.mark.usefixtures('setup')
class TestCheckoutPage:

    def test_positive_step_one_checkout(self):
        checkout_page = CheckoutPage(self.driver, 'standard_user', 'secret_sauce')
        checkout_page.enter_first_name('FirstName')
        checkout_page.enter_last_name('LastName')
        checkout_page.enter_postal_code('000000')
        checkout_page.click_continue()
        assert self.driver.current_url == 'https://www.saucedemo.com/checkout-step-two.html'

    @pytest.mark.parametrize('first_name, last_name, postal_code, expected_error_message',
                             [('', '', '', 'Error: First Name is required'),
                              ('FirstName', '', '', 'Error: Last Name is required'),
                              ('FirstName', 'LastName', '', 'Error: Postal Code is required')])
    def test_negative_step_one_checkout(self, first_name, last_name, postal_code, expected_error_message):
        checkout_page = CheckoutPage(self.driver, 'standard_user', 'secret_sauce')
        checkout_page.enter_first_name(first_name)
        checkout_page.enter_last_name(last_name)
        checkout_page.enter_postal_code(postal_code)
        checkout_page.click_continue()
        actual_error_message = checkout_page.read_error_message()
        assert actual_error_message == expected_error_message

    def test_cancel_checkout(self):
        checkout_page = CheckoutPage(self.driver, 'standard_user', 'secret_sauce')
        checkout_page.click_cancel()
        assert self.driver.current_url == 'https://www.saucedemo.com/cart.html'

    def test_complete_checkout(self):
        checkout_page = CheckoutPage(self.driver, 'standard_user', 'secret_sauce')
        checkout_page.enter_first_name('FirstName')
        checkout_page.enter_last_name('LastName')
        checkout_page.enter_postal_code('000000')
        checkout_page.click_continue()
        checkout_page.click_finish()
        checkout_page.click_back_home()
        assert self.driver.current_url == 'https://www.saucedemo.com/inventory.html'
