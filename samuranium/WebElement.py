from selenium.webdriver.remote.webelement import WebElement as we
from selenium.webdriver.common.by import By
from samuranium.utils.time import get_current_time
from samuranium.utils.logger import Logger
from timeit import default_timer as timer


class WebElement:
    """
    Web element class
    """
    def __init__(self, browser, selector, max_wait_time=30):
        self.browser = browser
        self.logger = Logger() # In the future this will be obtained from the core class so there is only 1 logger instance
        self.selector = selector
        self.max_wait_time = max_wait_time

    @property
    def element(self):
        """
        :return: web element
        """
        element: we = self.__find_element()
        return element

    @property
    def text(self):
        return self.element.text

    def __finder_strategies(self):
        return {'xpath': By.XPATH, 'css': By.CSS_SELECTOR, 'id': By.ID, 'class_name': By.CLASS_NAME,
                'link_text': By.LINK_TEXT, 'name': By.NAME}

    def __find_element(self):
        start_time = get_current_time()
        while timer() - start_time < self.max_wait_time:
            for strategy_name, method in self.__finder_strategies().items():
                try:
                    element: we = self.browser.find_element(method, self.selector)
                    return element
                except:
                    pass
        return None

    def is_displayed(self):
        return self.element.is_displayed()

    def click(self):
        try:
            self.element.click()
            return True
        except Exception as e:
            self.logger.error('Not possible to click on element with selector {}'.format(
                self.selector), e)
            return False

    def input_text(self, text):
        try:
            self.element.send_keys(text)
            return True
        except Exception as e:
            self.logger.error('Not possible to send text {} to element with selector {}'.format(
                text, self.selector), e)
            return False

