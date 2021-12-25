import pytest
from pages.inventory import InventoryPage


@pytest.mark.usefixtures('setup')
class TestInventoryPage:

    def test_adding_items_to_cart(self):
        inventory_page = InventoryPage(self.driver, 'standard_user', 'secret_sauce')
        inventory_page.add_all_items_to_cart()
        number_of_items = inventory_page.get_number_of_items()
        cart_badge = inventory_page.get_cart_badge()
        assert number_of_items == cart_badge

    def test_filtering_by_az(self):
        inventory_page = InventoryPage(self.driver, 'standard_user', 'secret_sauce')
        inventory_page.filter_items('Name (A to Z)')
        names = inventory_page.get_items_names()
        assert names == sorted(names)

    def test_filtering_by_za(self):
        inventory_page = InventoryPage(self.driver, 'standard_user', 'secret_sauce')
        inventory_page.filter_items('Name (Z to A)')
        names = inventory_page.get_items_names()
        assert names == sorted(names, reverse=True)

    def test_filtering_by_lh(self):
        inventory_page = InventoryPage(self.driver, 'standard_user', 'secret_sauce')
        inventory_page.filter_items('Price (low to high)')
        prices = inventory_page.get_items_prices()
        assert prices == sorted(prices)

    def test_filtering_by_hl(self):
        inventory_page = InventoryPage(self.driver, 'standard_user', 'secret_sauce')
        inventory_page.filter_items('Price (high to low)')
        prices = inventory_page.get_items_prices()
        assert prices == sorted(prices, reverse=True)
