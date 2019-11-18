import datetime
import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from samuranium.WebElement import WebElement
from samuranium.mobile import Mobile
from samuranium.utils.config import Config
from samuranium.utils.logger import Logger
from samuranium.reporter import Reporter
from samuranium.utils.paths import REPORT_SCREENSHOTS_PATH


class Samuranium:
    """
    Main class for Samuranium

    This is called when 'import Samuranium from samuraniun'
    """

    def __init__(self, context=None, selected_browser=None):
        """
        Initialization function
        Args:
            selected_browser: a string expecting browser name. Ex: 'chrome', 'firefox'
        """
        self.context = context
        self.config = Config(context)
        self.selected_browser = selected_browser if selected_browser else self.config.browser
        self.browser = self.__set_browser()
        self.logger = Logger()
        self.reporter = Reporter()
        self.selected_element = None
        if self.context:
            context.samuranium = self
            context.browser = self.browser

    def get_browser(self):
        """
        This function can be used if you want to use selenium web driver outside Samuranium

        Note:
            Not recommended!

        Returns:Webdriver Driver object which we call browser
        """
        return self.browser

    def __set_browser(self):
        """
        Private method that sets the selected browser
        Returns: Webdriver element

        """
        return {'chrome': self.__get_chrome, 'firefox': self.__get_firefox,
                'android-browser': self.__get_android_browser}.get(self.selected_browser)()

    def __get_android_browser(self):
        return Mobile(self).get_driver()

    def __get_chrome(self):
        """
        Private method that starts webdriver.Chrome
        Returns: webdriver.Chrome
        """
        return webdriver.Chrome(executable_path=ChromeDriverManager().install())

    def __get_firefox(self):
        """
        Private method that starts webdriver.Firefox
        Returns: webdriver.Firefox
        """
        return webdriver.Firefox(executable_path=GeckoDriverManager().install())

    def navigate_to_url(self, url):
        """
        Navigates to a given url
        Args:
            url: url string
        """
        self.browser.get(url)

    def get_title(self):
        """
        Returns:Current's web page title
        """

        return self.browser.title

    def wait_for_element(self, selector):
        """
        Waits for an element to be found and verifies it is displayed
        Sets the element to self.selected_element so you can use it before action methods like click_on_element
        If the element is not found, if will raise an Exception

        Args:
            selector: Any valid selector

        Returns: Boolean for element.is_displayed()

        """
        self.selected_element = WebElement(self, selector)
        self.selected_element.ensure_element_exists()
        return self.selected_element.is_displayed()

    def find_element(self, selector, exact_selector=False):
        """
        Finds an element by the given selector

        Sets the element to self.selected_element so you can use it before action methods like click_on_element

        Warnings:
            Triggers a NoSuchElementException if not found
        Args:
            selector: Any valid selector

        Returns: WebElement
        """
        self.selected_element: WebElement = WebElement(self, selector, exact_selector=exact_selector)
        self.selected_element.ensure_element_exists()
        return self.selected_element

    def click_on_element(self, selector=None, exact_selector=False):
        """
        Clicks on an element by a given selector
        If no selector is passed, it will try to click on self.selected_element, set by find_element for instance

        Args:
            selector: Any valid selector
        """
        if selector:
            self.find_element(selector, exact_selector)
        self.selected_element.click()

    def input_text_on_element(self, text, selector=None):
        """
        Inputs text on a element with a given selector
        If no selector is passed, it will try to click on self.selected_element, set by find_element for instance
        Args:
            text: A string to be typed in the element
            selector: (optional) Any valid selector.
        """
        if selector:
            self.find_element(selector)
        self.selected_element.input_text(text)

    def press_enter_key(self):
        """
        Send Keys.Enter to the selected element

        Note:
            An element must be selected using find_element or wait_for_element first

        """
        if self.selected_element:
            self.selected_element.input_text(Keys.ENTER)
        else:
            raise Exception('No selected element. Impossible to input text. An element must be selected first')

    def press_backspace_key(self, times=1):
        """
        Send Keys.BACKSPACE to the selected element

        Note:
            An element must be selected using find_element or wait_for_element first

        Args:
            times: (optional)  How many times should the Backspace key be pressed. Default = 1

        """
        for _ in range(0, times):
            self.selected_element.input_text(Keys.BACKSPACE)

    def save_screenshot(self, name=None, output_folder=None):
        if not output_folder:
            output_folder = REPORT_SCREENSHOTS_PATH
        if not name:
            name = 'randomvalue.png'
        if not name.endswith('.png'):
            name = '{}.png'.format(name)
        screenshot_path = os.path.join(output_folder, name)
        os.makedirs(output_folder, exist_ok=True)
        self.browser.save_screenshot(screenshot_path)

    def save_error_screenshot(self, step):
        output_folder = REPORT_SCREENSHOTS_PATH
        os.makedirs(output_folder, exist_ok=True)
        screenshot_name = '{}.png'.format(str(datetime.datetime.now().strftime("%Y%m%d_%H-%M-%S")))
        screenshot_path = os.path.join(output_folder, screenshot_name)
        self.browser.save_screenshot(screenshot_path)
        step.screenshot = screenshot_path


    def tear_down(self):
        """
        Closes the browser and sets self.browser = None
        """
        try:
            os.environ.pop('VERSION')
        except Exception:
            pass
        self.browser.quit()
        self.browser = None
