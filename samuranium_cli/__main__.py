import os

from samuranium_cli.bdd import create_bdd_project
from samuranium_cli.templates import samuranium_config_file_string
from samuranium_cli.utils import get_working_directory


def create_config_files():
    samuranium_config_file = os.path.join(get_working_directory(), '.samuranium')
    with open(samuranium_config_file, 'w') as file:
        file.write(samuranium_config_file_string)


def main():
    steps = ['config files', 'bdd']
    for index, step in enumerate(steps, start=1):
        print("Step {}/{}: {}".format(index, len(steps), step))
        {'config files': create_config_files, 'bdd': create_bdd_project}.get(step)()


if __name__ == '__main__':
    main()

create_config_files()