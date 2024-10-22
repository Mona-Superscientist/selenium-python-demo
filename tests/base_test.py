# utils/base_class.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import os


def initialize_driver():
    browser = os.getenv('BROWSER', 'chrome')  # Default to Chrome
    if browser == 'chrome':
        service = ChromeService(ChromeDriverManager().install())
        return webdriver.Chrome(service=service)
    elif browser == 'firefox':
        service = FirefoxService(GeckoDriverManager().install())
        return webdriver.Firefox(service=service)
    else:
        raise ValueError("Unsupported browser: {}".format(browser))


class BaseTest:

    @pytest.fixture(scope="class")
    def setup(self, request):
        self.driver = initialize_driver()
        self.driver.maximize_window()
        request.cls.driver = self.driver
        yield
        self.driver.quit()
