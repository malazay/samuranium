### This file is a work in progress, use with precaution

import argparse

from behave.__main__ import main as behave_runner
from behave.__main__ import TAG_HELP
from samuranium.utils.paths import REPORT_PATH
from samuranium.utils.config import Config


def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('-b', '--browser', help='Which browser should run. Ex: chrome, firefox')
    parser.add_argument('-t', '--tags', help=TAG_HELP)
    return parser.parse_args()


def samuranium_runner():
    args = parse_args()
    parsed_args = '-f allure_behave.formatter:AllureFormatter -o ./reports ./features '
    if args.tags:
        parsed_args += '--tags={} '.format(args.tags)
    if args.browser:
        parsed_args += '-D browser={} '.format(args.browser)
    behave_runner(parsed_args)



