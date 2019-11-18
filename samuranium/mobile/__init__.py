from appium import webdriver

from samuranium.mobile.AppiumServerManager import AppiumServerManager


class Mobile:
    def __init__(self, samuranium):
        self.samuranium = samuranium
        self.appium_server = AppiumServerManager(samuranium)
        self.mobile_driver = None

    @property
    def caps(self):
        return {'android-browser': self.__get_android_browser_caps}.get(self.samuranium.selected_browser)()

    def get_driver(self):
        self.appium_server.start()
        self.mobile_driver = webdriver.Remote('http://127.0.0.1:{}/wd/hub'.format(self.appium_server.port), self.caps)
        return self.mobile_driver

    def __get_android_browser_caps(self):
        caps = {
            'deviceName': self.samuranium.config.get_property('mobile', 'android_device_name'),
            'platformName': 'android',
            'platformVersion': self.samuranium.config.get_property('mobile', 'android_platform_version'),
            'browserName': 'chrome'
        }

        return caps

    def __get_android_app(self):
        pass

    def __get_ios_browser(self):
        pass

    def __get_ios_app(self):
        pass