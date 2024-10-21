from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from pages.base_page import BasePage
from utils import load_env

base_url = load_env.base_url


class SignupPage(BasePage):
    def __init__(self):
        super().__init__()

    # Elements
    locators = {
        'page_title': (By.TAG_NAME, 'h1'),
        'page_description': (By.TAG_NAME, 'p'),
        'first_name_input': (By.ID, 'firstname'),
        'last_name_input': (By.ID, 'lastname'),
        'email_input': (By.ID, 'email'),
        'password_input': (By.ID, 'password'),
        'submit_btn': (By.ID, 'submit'),
        'cancel_btn': (By.ID, 'cancel')
    }

    # Actions
    def navigate(self):
        self.driver.get(f'{base_url}/addUser')

    def enter_first_name(self, first_name):
        self.driver.find_element(*self.locators['first_name_input']).send_keys(first_name)

    def enter_last_name(self, last_name):
        self.driver.find_element(*self.locators['last_name_input']).send_keys(last_name)

    def enter_email(self, email):
        self.driver.find_element(*self.locators['email_input']).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(*self.locators['password_input']).send_keys(password)

    def click_submit(self):
        self.driver.find_element(*self.locators['submit_btn']).click()

    def click_cancel(self):
        self.driver.find_element(*self.locators['cancel_btn']).click()

    # Assertions
    def page_title_displayed_correctly(self, expected_text):
        try:
            actual_text = self.driver.find_element(*self.locators['page_title']).text
            return actual_text == expected_text
        except NoSuchElementException:
            return False

    def is_current_url_equals(self, expected_url):
        return self.driver.current_url == expected_url