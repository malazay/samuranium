import os
import sys

from samuranium.utils.general import is_android_device_connected

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pyunitreport import HTMLTestRunner
import unittest

from samuranium import Samuranium

DEVICE_ONLINE = is_android_device_connected()

@unittest.skipUnless(DEVICE_ONLINE, 'No Android device attached')
class AndroidBrowserTest(unittest.TestCase):
    def setUp(self):
        self.samuranium = Samuranium(selected_browser='android-browser')
        self.search_text = 'Michael Jordan'

    def test_search_wikipedia(self):
        self.assertIsNotNone(self.samuranium.get_browser(),
                             'Browser "{}" does not exist'.format(self.samuranium.selected_browser))
        self.samuranium.navigate_to_url('http://www.wikipedia.org')
        self.assertTrue(self.samuranium.wait_for_element('#js-link-box-en'), 'Element not displayed')
        title = self.samuranium.get_title()
        self.assertEqual(title, 'Wikipedia', 'Expected: {} found: {}'.format('Wikipedia', title))
        self.samuranium.click_on_element('#js-link-box-en')
        assert self.samuranium.find_element('searchIcon'), 'Search button not found'
        self.samuranium.click_on_element() # If no selector is passed, samuranium will click on the latest found element
        # in this case: "seachIcon"
        assert self.samuranium.find_element('.search:not([readonly])'), 'Search box not found'
        self.samuranium.input_text_on_element(self.search_text)
        assert self.samuranium.find_element(".results [title='{}']".format(self.search_text)), \
            'Search results page not found'

    def tearDown(self) -> None:
        self.samuranium.tear_down()


if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output='output'))