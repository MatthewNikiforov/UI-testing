from pages.base import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        self.url = 'https://www.saucedemo.com/'
        self.driver = driver
        super().__init__(self.driver, self.url)

    def enter_username(self, username):
        username_input = self.find_element_if_present('id', 'user-name')
        username_input.send_keys(username)

    def enter_password(self, password):
        password_input = self.find_element_if_present('id', 'password')
        password_input.send_keys(password)

    def click_login_button(self):
        login_button = self.find_element_if_present('id', 'login-button')
        login_button.click()

    def read_error_message(self):
        error_message = self.find_element_if_present('tag_name', 'h3').text
        return error_message
