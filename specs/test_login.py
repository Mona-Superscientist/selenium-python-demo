import unittest
from specs.base_test import BaseTest


class TestLogin(BaseTest):

    def test_login(self):
        self.home_page.navigate()
        self.home_page.enter_email('test@gmail.com')
        self.home_page.enter_password('pass')
        self.home_page.click_submit()

        self.assertTrue(self.home_page.assertAppTitleIsDisplayed())


if __name__ == "__main__":
    unittest.main()
