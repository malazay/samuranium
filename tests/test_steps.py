import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pyunitreport import HTMLTestRunner
import unittest

from samuranium import Samuranium
from samuranium.steps import navigate_to_url, verify_page_title, wait_for_element, click_on_element, \
    write_text_on_element

class ContextMock:
    """
    This is a Mock class for Behave's Context class

    Needed to call any Behave steps outside the Behave runner
    """
    def __init__(self):
        """
        We create the Samuranium instance here so it's passed down to the steps definitions
        """
        self.samuranium = Samuranium(selected_browser='chrome')


class StepsTest(unittest.TestCase):
    def setUp(self):
        self.context = ContextMock()
        self.search_text = 'Michael Jordan'
        navigate_to_url(self.context, 'http://www.wikipedia.org')

    def test_verify_page_title(self):
        verify_page_title(self.context, 'Wikipedia')

    def test_element_finding(self):
        wikipedia_logo_selector = 'central-featured'
        assert wait_for_element(self.context, wikipedia_logo_selector), \
            'Error: Selector {} not found'.format(wikipedia_logo_selector)

    def test_element_clicking(self):
        click_on_element(self.context, 'English')
        verify_page_title(self.context, 'Wikipedia, the free encyclopedia')

    def test_input_text(self):
        self.test_element_clicking()
        write_text_on_element(self.context, self.search_text, 'searchInput')
        click_on_element(self.context, 'searchButton')
        header = self.context.samuranium.find_element("//h1[text()='{}']".format(self.search_text))
        self.assertTrue(self.search_text in header.text, '{} not found'.format(self.search_text))

    def tearDown(self) -> None:
        self.context.samuranium.tear_down()

if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output='output'))