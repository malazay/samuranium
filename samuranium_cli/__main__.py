import os

from samuranium_cli.bdd import create_bdd_project


def setup():
    print("Running setup. Empty for now")
    pass


def create_config_files():
    print("Running config files. Empty for now")
    pass


def create_output_folder():
    print("Running output folder. Empty for now")
    pass


def get_working_directory():
    return os.getcwd()


def main():
    steps = ['setup', 'config files', 'output folders', 'bdd']
    for index, step in enumerate(steps, start=1):
        print("Step {}/{}: {}".format(index, len(steps), step))
        {'setup': setup, 'config files': create_config_files,
         'output folders': create_output_folder, 'bdd': create_bdd_project}.get(step)()


if __name__ == '__main__':
    main()
