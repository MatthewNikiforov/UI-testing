from selenium.webdriver.support.select import Select
from pages.base import BasePage
from pages.login import LoginPage


class InventoryPage(BasePage):

    def __init__(self, driver, username, password):
        self.__login_page = LoginPage(driver)
        self.__login_page.enter_username(username)
        self.__login_page.enter_password(password)
        self.__login_page.click_login_button()
        super().__init__(self.__login_page.driver, self.__login_page.driver.current_url)

    def filter_items(self, option):
        select_element = self.find_element_if_present('tag_name', 'select')
        select_object = Select(select_element)
        select_object.select_by_visible_text(option)

    def add_all_items_to_cart(self):
        add_buttons = self.find_elements_if_present('class_name', 'btn_inventory')
        for add_button in add_buttons:
            add_button.click()

    def get_number_of_items(self):
        items = self.find_elements_if_present('class_name', 'inventory_item')
        return len(items)

    def get_items_names(self):
        items_names = self.find_elements_if_present('class_name', 'inventory_item_name')
        names = list(map(lambda item_name: item_name.text, items_names))
        return names

    def get_items_prices(self):
        items_prices = self.find_elements_if_present('class_name', 'inventory_item_price')
        prices = list(map(lambda item_price: float(item_price.text[1:]), items_prices))
        return prices

    def get_cart_badge(self):
        cart_badge = self.find_element_if_present('class_name', 'shopping_cart_badge').text
        return int(cart_badge)

    def switch_to_cart(self):
        cart_link = self.find_element_if_present('class_name', 'shopping_cart_link')
        cart_link.click()
