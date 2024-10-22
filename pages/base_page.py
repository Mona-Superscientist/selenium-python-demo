from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element_to_be_visible(self, by, value, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((by, value))
            )
        except TimeoutException:
            print(f"Element located by {by}='{value}' not visible after {timeout} seconds.")
            raise

    def wait_for_url_to_change(self, old_url, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.url_changes(old_url)
        )
