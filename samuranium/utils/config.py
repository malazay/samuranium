import configparser
import os

from samuranium.utils.paths import PROJECT_ROOT_PATH


class Config:
    def __init__(self, context=None):
        self.config_file_location = os.path.join(PROJECT_ROOT_PATH, '.samuranium')
        self.config = configparser.ConfigParser()
        self.config.read(self.config_file_location)
        self.context = context

    @property
    def cli_params(self):
        if self.context:
            return self.context.config.userdata
        return []

    @property
    def is_mobile(self):
        return True

    @property
    def browser(self):
        if self.cli_params:
            cli_browser = self.cli_params.get('browser', None)
            if cli_browser:
                return cli_browser
        return self.get_property('browser', 'browser')

    @property
    def default_wait_time(self):
        default_wait_time = 30
        return self.get_property('browser', 'wait_time') or default_wait_time

    def get_property(self, category, property):
        try:
            return self.config.get(category, property).replace('"', '').replace("'", '')
        except:
            return None