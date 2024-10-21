from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

import os


def initialize_driver():
    # Use webdriver-manager to install drivers automatically
    browser = os.getenv('BROWSER', 'chrome')  # Default to chrome
    if browser == 'chrome':
        service = ChromeService(ChromeDriverManager().install())
        return webdriver.Chrome(service=service)
    elif browser == 'firefox':
        service = FirefoxService(GeckoDriverManager().install())
        return webdriver.Firefox(service=service)
    else:
        raise ValueError("Unsupported browser: {}".format(browser))


class BasePage:
    def __init__(self):
        self.driver = initialize_driver()

    def wait_for_element_to_be_visible(self, by, value, timeout=10):
        """Wait for an element to be visible."""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((by, value))
            )
        except TimeoutException:
            print(f"Element located by {by}='{value}' not visible after {timeout} seconds.")
            raise

    def wait_for_url_to_change(self, old_url, timeout=10):
        """Wait for the URL to change."""
        WebDriverWait(self.driver, timeout).until(
            EC.url_changes(old_url)
        )

    def quit_driver(self):
        self.driver.quit()
