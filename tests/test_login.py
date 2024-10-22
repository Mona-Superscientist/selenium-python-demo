import pytest
import allure

from pages.home_page import HomePage
from tests.base_test import BaseTest


@allure.feature("Login features")
@pytest.mark.usefixtures("setup")
class TestLogin(BaseTest):

    @allure.title("successful login test")
    def test_login(self):
        self.home_page = HomePage(self.driver)

        self.home_page.navigate()
        self.home_page.enter_email('test@gmail.com')
        self.home_page.enter_password('pass')
        self.home_page.click_submit()

        assert self.home_page.assertAppTitleIsDisplayed()
