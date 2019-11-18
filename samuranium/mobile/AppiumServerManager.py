import os
import time

import requests

from samuranium.utils.general import get_random_port, run_command
from webdriver_manager.chrome import ChromeDriverManager


class AppiumServerManager:
    def __init__(self, samuranium):
        self.config = samuranium.config
        self.appium_command = 'appium'
        self.port = None
        self.logs_port = None
        self.process = None
        self.pid = None
        self.chromedriver_version = self.config.get_property('mobile', 'chromedriver')


    def is_running(self):
        try:
            _status_request = requests.get('http://127.0.0.1:{}/wd/hub/status'.format(self.port))
            return _status_request.status_code == 200 and _status_request.json().get('status') == 0
        except:
            return False

    @property
    def chromedriver_path(self):
        if self.chromedriver_version:
            os.environ['VERSION'] = self.chromedriver_version
            return ChromeDriverManager().install()
        return None

    def _wait_until_ready(self):
        max_wait_time = 0
        while not self.is_running() and max_wait_time <= 30:
            time.sleep(5)
        print("Server started")

    def start(self):
        self.port = get_random_port()
        self.logs_port = get_random_port()
        command = '{} -p {} -G 0.0.0.0:{} '.format(self.appium_command, self.port,  self.logs_port)
        if self.chromedriver_path:
            command = '{} --chromedriver-executable {}'.format(command, self.chromedriver_path)
        self.process = run_command(command)
        self.pid = self.process.pid
        self._wait_until_ready()

    def stop(self):
        self.process.kill()
        self.process = None
        self.pid = None
