from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from samuranium.WebElement import WebElement
from samuranium.utils.logger import Logger
from samuranium.reporter import Reporter

class Samuranium:
    """
    Main class for Samuranium

    This is called when 'import Samuranium from samuraniun'
    """
    def __init__(self, selected_browser='chrome'):
        """
        Initialization function
        Args:
            selected_browser: a string expecting browser name. Ex: 'chrome', 'firefox'
        """
        self.selected_browser = selected_browser
        self.browser = self.__set_browser()
        self.logger = Logger()
        self.reporter = Reporter()
        self.selected_element = None

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
        return {'chrome': self.__get_chrome, 'firefox': self.__get_firefox}.get(self.selected_browser)()

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
        self.selected_element = WebElement(self.browser, selector)
        if not self.selected_element:
            raise Exception("Element not found") # Todo handle this exception properly :D
        return self.selected_element.is_displayed()

    def find_element(self, selector):
        """
        Finds an element by the given selector

        Sets the element to self.selected_element so you can use it before action methods like click_on_element
        Args:
            selector: Any valid selector

        Returns: WebElement
        """
        self.selected_element: WebElement = WebElement(self.browser, selector)
        return self.selected_element

    def click_on_element(self, selector=None):
        """
        Clicks on an element by a given selector
        If no selector is passed, it will try to click on self.selected_element, set by find_element for instance

        Args:
            selector: Any valid selector
        """
        if selector:
            self.selected_element = WebElement(self.browser, selector)
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
            self.selected_element = WebElement(self.browser, selector)
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

    def tear_down(self):
        """
        Closes the browser and sets self.browser = None
        """
        self.browser.quit()
        self.browser = None
