import yaml
import argparse

def open_file(filename):
    """Function opens file and returns file descriptor."""
    f = open(filename,'r')
    return f

def load_yaml(filename):
    """Function to read config file"""
    configfd = open_file(filename)
    if configfd:
        config = yaml.load(configfd)
        return config
    return None

def handle_config(config_file):
    """Load user configuration files"""

    if config_file:
        ret = load_yaml(config_file)
        return ret

    return False


def parse_args():
    """Parse arguments with newer argparse module
        (adds built-in required parm)
    """
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        description='Create config hashmap based on config file')
    parser.add_argument("-c", "--config",
                        help="Config file(s) to read.",
                        action="store", dest="config_file",
                        default=None)
    return parser.parse_args()


def generate_config_hashmap():
    """Function to generate hashmap"""

    args = parse_args()

    if args.config_file:
        config_hashmap = handle_config(args.config_file)
        return config_hashmap

