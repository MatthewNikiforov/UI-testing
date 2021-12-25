from pages.base import BasePage
from pages.inventory import InventoryPage


class CartPage(BasePage):

    def __init__(self, driver, username, password):
        self.__inventory_page = InventoryPage(driver, username, password)
        self.__inventory_page.add_all_items_to_cart()
        self.__inventory_page.switch_to_cart()
        super().__init__(self.__inventory_page.driver, self.__inventory_page.driver.current_url)

    def back_to_inventory(self):
        back_button = self.find_element_if_present('id', 'continue-shopping')
        back_button.click()

    def get_number_of_items(self):
        items = self.find_elements_if_present('class_name', 'cart_item')
        return len(items)

    def remove_item(self, item_number):
        remove_buttons = self.find_elements_if_present('class_name', 'cart_button')
        if (item_number >= 0) and (item_number <= len(remove_buttons) - 1) and (len(remove_buttons) > 0):
            remove_buttons[item_number].click()

    def checkout(self):
        checkout_button = self.find_element_if_present('id', 'checkout')
        checkout_button.click()
