import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def setup(request):
    driver = webdriver.Chrome()
    request.cls.driver = driver
    yield
    driver.quit()
