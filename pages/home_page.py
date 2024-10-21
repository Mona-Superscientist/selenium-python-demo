from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from pages.base_page import BasePage
from utils import load_env

base_url = load_env.base_url


class HomePage(BasePage):
    def __init__(self):
        super().__init__()

    # Elements
    locators = {
        'page_title': (By.TAG_NAME, "h1"),
        'email_input': (By.ID, "email"),
        'password_input': (By.ID, "password"),
        'submit_button': (By.ID, "submit"),
        'signup_button': (By.ID, "signup"),
        'error_span': (By.ID, "error")
    }

    # Actions
    def navigate(self):
        self.driver.get(f'{base_url}')

    def enter_email(self, email):
        self.driver.find_element(*self.locators['email_input']).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(*self.locators['password_input']).send_keys(password)

    def click_submit(self):
        self.driver.find_element(*self.locators['submit_button']).click()

    def click_signup(self):
        self.driver.find_element(*self.locators['signup_button']).click()

    # Assertions
    def assertAppTitleIsDisplayed(self):
        try:
            return self.driver.find_element(*self.locators['page_title']).is_displayed()
        except NoSuchElementException:
            return False
