from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.driver.get(self.url)
        self.wait = WebDriverWait(self.driver, 15)

    def __find_by(self, by: str):
        by = by.lower()
        locating = {'css': By.CSS_SELECTOR,
                    'xpath': By.XPATH,
                    'class_name': By.CLASS_NAME,
                    'id': By.ID,
                    'link_text': By.LINK_TEXT,
                    'name': By.NAME,
                    'partial_link_text': By.PARTIAL_LINK_TEXT,
                    'tag_name': By.TAG_NAME}
        return locating[by]

    def find_element_if_present(self, by, locator):
        return self.wait.until(ec.presence_of_element_located((self.__find_by(by), locator)))

    def find_elements_if_present(self, by, locator):
        return self.wait.until(ec.presence_of_all_elements_located((self.__find_by(by), locator)))
