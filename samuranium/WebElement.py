import time

from selenium.webdriver.remote.webelement import WebElement as we
from selenium.webdriver.common.by import By
from samuranium.utils.time import get_current_time
from timeit import default_timer as timer
from selenium.common.exceptions import NoSuchElementException


class WebElement:
    """
    Web element class
    """
    def __init__(self, samuranium, selector, exact_selector=False, max_wait_time=None):
        self.samuranium = samuranium
        self.browser = self.samuranium.browser
        self.logger = self.samuranium.logger
        self.selector = selector
        self.exact_selector = exact_selector
        self.max_wait_time = max_wait_time if max_wait_time else float(self.samuranium.config.default_wait_time)

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

    def is_present(self):
        return self.element is not None


    def ensure_element_exists(self):
        if not self.is_present():
            raise NoSuchElementException('Element with selector "{}" was not found after {} seconds'.
                                         format(self.selector, self.max_wait_time))

    def __finder_strategies(self):
        return {'xpath': By.XPATH, 'css': By.CSS_SELECTOR, 'id': By.ID, 'class_name': By.CLASS_NAME,
                'link_text': By.LINK_TEXT, 'name': By.NAME}

    def __xpath_strategies(self):
        return {'match_xpath': '{}','exact_text': '//*[text()="{}"]',
                'normalize_text': '//*[text()[normalize-space()="{}"]]'}

    def __css_strategies(self):
        return {'match_css': '{}', 'class_name': '.{}', 'id': '#{}'}

    def __find_element(self):
        start_time = get_current_time()
        while timer() - start_time < self.max_wait_time:
            for strategy_name, method in self.__finder_strategies().items():
                try:
                    if strategy_name == 'xpath':
                        element: we =  self.__find_by_xpath()
                        if element:
                            return element
                    elif strategy_name == 'css':
                        element: we = self.__find_by_css_selector()
                        if element:
                            return element
                    if not self.exact_selector:
                        element: we = self.browser.find_element(method, self.selector)
                        return element
                except:
                    pass
        return None

    def __find_by_xpath(self):
        for finder_name, xpath_strategy in self.__xpath_strategies().items():
            try:
                if self.exact_selector:
                    return self.browser.find_element_by_xpath(self.selector)
                return self.browser.find_element_by_xpath(xpath_strategy.format(self.selector))
            except NoSuchElementException:
                pass
        return None

    def __find_by_css_selector(self):
        for finder_name, css_stragegy in self.__css_strategies().items():
            try:
                if self.exact_selector:
                    return self.browser.find_element_by_css_selector(self.selector)
                return self.browser.find_element_by_css_selector(css_stragegy.format(self.selector))
            except NoSuchElementException:
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
        for _ in range(5):
            try:
                self.element.send_keys(text)
                return True
            except Exception as e:
                self.logger.error('Not possible to send text {} to element with selector {}'.format(
                    text, self.selector), e)
                self.logger.debug("Waiting 1 second until element is interactable")
                time.sleep(1)
        return False

