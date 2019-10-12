import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pyunitreport import HTMLTestRunner
import unittest

from samuranium import Samuranium


class SimpleTest(unittest.TestCase):
    def setUp(self):
        pass

    def search_wikipedia(self):
        self.assertIsNotNone(self.samuranium.get_browser(),
                             'Browser "{}" does not exist'.format(self.samuranium.selected_browser))
        self.samuranium.navigate_to_url('http://www.wikipedia.org')
        title = self.samuranium.get_title()
        self.assertEqual(title, 'Wikipedia', 'Expected: {} found: {}'.format('Wikipedia', title))
        self.assertTrue(self.samuranium.wait_for_element('#js-link-box-en'), 'Element not displayed')
        self.samuranium.click_on_element('#js-link-box-en')
        self.assertTrue(self.samuranium.find_element('mp-topbanner'), 'banner not found')
        self.samuranium.input_text_on_element('Michael Jordan', '#searchInput')
        self.samuranium.click_on_element('#searchButton')
        header = self.samuranium.find_element('#firstHeading')
        self.assertTrue('Michael Jordan' in header.text, 'Jordan not found')

    def test_chrome(self):
        self.samuranium = Samuranium()
        self.search_wikipedia()

    def test_firefox(self):
        self.samuranium = Samuranium(selected_browser='firefox')
        self.search_wikipedia()

    def tearDown(self) -> None:
        self.samuranium.tear_down()


if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output='output'))