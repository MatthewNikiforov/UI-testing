import pytest
from pages.login import LoginPage


@pytest.mark.usefixtures('setup')
class TestLoginPage:

    def test_positive_login(self):
        login_page = LoginPage(self.driver)
        login_page.enter_username('standard_user')
        login_page.enter_password('secret_sauce')
        login_page.click_login_button()
        assert self.driver.current_url == 'https://www.saucedemo.com/inventory.html'

    @pytest.mark.parametrize('username, password, error_message',
                            [('', '', 'Epic sadface: Username is required'),
                            ('', '0000', 'Epic sadface: Username is required'),
                            ('name', '', 'Epic sadface: Password is required'),
                            ('locked_out_user', 'secret_sauce', 'Epic sadface: Sorry, this user has been locked out.')])
    def test_negative_login(self, username, password, error_message):
        login_page = LoginPage(self.driver)
        login_page.enter_username(username)
        login_page.enter_password(password)
        login_page.click_login_button()
        assert login_page.read_error_message() == error_message
