import unittest

from page_objects import MainPage
from page_objects import DriverService


class TestMainPage(unittest.TestCase):

    def setUp(self):
        self.service = DriverService()
        self.driver = self.service.configure_driver()

    def tearDown(self):
        self.service.close()

    def test_search(self):
        main_page = MainPage(self.driver)
        main_page.go_to_main_page()
        main_page.fill_postcode('BLA')
        main_page.click_green_button()

