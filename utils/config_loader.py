from os.path import dirname, realpath
import yaml


def read_yaml(config):
    with open(f'config/{config}', 'r') as config_file:
        config_dictionary = yaml.load(config_file, Loader=yaml.FullLoader)
        return config_dictionary