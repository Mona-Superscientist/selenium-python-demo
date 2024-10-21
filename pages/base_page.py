from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
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

    def quit_driver(self):
        self.driver.quit()
