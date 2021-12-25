import pytest
from pages.cart import CartPage


@pytest.mark.usefixtures('setup')
class TestCartPage:

    def test_back_to_inventory(self):
        cart_page = CartPage(self.driver, 'standard_user', 'secret_sauce')
        cart_page.back_to_inventory()
        assert self.driver.current_url == 'https://www.saucedemo.com/inventory.html'

    def test_removing_item(self):
        cart_page = CartPage(self.driver, 'standard_user', 'secret_sauce')
        number_of_items_before_removal = cart_page.get_number_of_items()
        cart_page.remove_item(0)
        number_of_items_after_removal = cart_page.get_number_of_items()
        assert number_of_items_after_removal == number_of_items_before_removal - 1

    def test_checkout(self):
        cart_page = CartPage(self.driver, 'standard_user', 'secret_sauce')
        cart_page.checkout()
        assert self.driver.current_url == 'https://www.saucedemo.com/checkout-step-one.html'
