import os

from samuranium_cli.templates import env_file_string, sample_steps_file_string, sample_feature_file_string


def get_working_directory():
    return os.getcwd()


def create_bdd_files(features_folder_path, steps_folder_path):
    env_file_path = os.path.join(features_folder_path, 'environment.py')
    sample_feature_file_path = os.path.join(features_folder_path, 'sample.feature')
    sample_steps_file_path = os.path.join(steps_folder_path, 'steps.py')
    with open(env_file_path, 'w') as file:
        file.write(env_file_string)
    with open(sample_feature_file_path, 'w') as file:
        file.write(sample_feature_file_string)
    with open(sample_steps_file_path, 'w') as file:
        file.write(sample_steps_file_string)


def create_bdd_project():
    print('Creating bdd project structure')
    features_path = os.path.join(get_working_directory(), 'features')
    steps_path = os.path.join(features_path, 'steps')
    os.makedirs(steps_path, exist_ok=True)
    create_bdd_files(features_path, steps_path)