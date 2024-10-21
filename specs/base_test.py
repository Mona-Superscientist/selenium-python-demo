import unittest
from pages.home_page import HomePage


class BaseTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.home_page = HomePage()

    @classmethod
    def tearDownClass(cls):
        cls.home_page.quit_driver()
