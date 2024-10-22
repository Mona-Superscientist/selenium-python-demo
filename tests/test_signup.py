import pytest
import allure
from pages.signup_page import SignupPage
from tests.base_test import BaseTest
from constants import routes
from utils import data_generator, json_utils


@allure.feature('signup')
@pytest.mark.usefixtures("setup")
class TestSignup(BaseTest):

    @allure.title('successful signup testcase')
    def test_successful_signup(self):
        self.signup_page = SignupPage(self.driver)

        self.signup_page.navigate()
        self.signup_page.enter_first_name(data_generator.generate_random_name())
        self.signup_page.enter_last_name(data_generator.generate_random_name())
        self.signup_page.enter_email(data_generator.generate_random_email())
        self.signup_page.enter_password(data_generator.generate_random_password())
        self.signup_page.click_submit()

        assert self.signup_page.is_current_url_equals(routes.contacts_list_url)

    # Example for parametrized tests using json file
    @allure.title('invalid signup tests')
    @pytest.mark.parametrize("data", json_utils.load_json_data('signup_invalid_data.json'))
    def test_invalid_signups(self, data):
        self.signup_page = SignupPage(self.driver)

        self.signup_page.navigate()
        self.signup_page.enter_first_name(data_generator.generate_random_name())
        self.signup_page.enter_last_name(data_generator.generate_random_name())
        self.signup_page.enter_email(data['email'])
        self.signup_page.enter_password(data['password'])
        self.signup_page.click_submit()

        # Get the actual error message
        assert self.signup_page.is_error_equals(data['expected_error'])
