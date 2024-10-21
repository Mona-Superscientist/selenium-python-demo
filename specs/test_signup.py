import unittest

from pages.signup_page import SignupPage
from specs.base_test import BaseTest
from utils import data_generator


class TestSignup(BaseTest):

    @classmethod
    def setUpClass(cls):
        cls.signup_page = SignupPage()

    def test_successful_signup(self):
        self.signup_page.navigate()
        self.signup_page.enter_first_name(data_generator.generate_random_name())
        self.signup_page.enter_last_name()(data_generator.generate_random_name())
        self.signup_page.enter_email(data_generator.generate_random_email())
        self.signup_page.enter_password(data_generator.generate_random_password())
        self.signup_page.click_submit()


if __name__ == "__main__":
    unittest.main()
