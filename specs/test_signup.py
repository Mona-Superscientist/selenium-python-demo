import unittest

from pages.signup_page import SignupPage
from specs.base_test import BaseTest
from constants import routes
from utils import data_generator, json_utils


class TestSignup(BaseTest):

    @classmethod
    def setUpClass(cls):
        cls.signup_page = SignupPage()

    @classmethod
    def tearDownClass(cls):
        cls.signup_page.quit_driver()

    def test_successful_signup(self):
        self.signup_page.navigate()
        self.signup_page.enter_first_name(data_generator.generate_random_name())
        self.signup_page.enter_last_name(data_generator.generate_random_name())
        self.signup_page.enter_email(data_generator.generate_random_email())
        self.signup_page.enter_password(data_generator.generate_random_password())
        self.signup_page.click_submit()

        self.assertTrue(self.signup_page.is_current_url_equals(routes.contacts_list_url))

    # Example for parametrized tests using json file
    def test_invalid_signups(self):
        # Load invalid data from JSON file using the utility function
        invalid_data = json_utils.load_json_data('signup_invalid_data.json')

        for data in invalid_data:
            with self.subTest(data=data):  # Allows separate reporting for each case
                self.signup_page.navigate()
                self.signup_page.enter_first_name(data_generator.generate_random_name())
                self.signup_page.enter_last_name(data_generator.generate_random_name())
                self.signup_page.enter_email(data['email'])
                self.signup_page.enter_password(data['password'])
                self.signup_page.click_submit()

                # Get the actual error message
                self.assertTrue(self.signup_page.is_error_equals(data['expected_error']))


if __name__ == "__main__":
    unittest.main()
