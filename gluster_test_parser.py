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
        config = yaml.load(configfd, Loader=yaml.FullLoader)
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

def get_server_ip(server_name,config_hashmap):
    """ Gives the server ip given the server name
    Args:
        server_name: name of the server as in config file.
                     example: server_vm1
        config_hashmap: the config file dictionary generated
                        while parsing.
    Returns:
        ip address of the given server
    Example:
        get_server_ip("server_vm1",config_hashmap)
    """
    index = server_name[9:]
    server_ip = config_hashmap['servers'][int(index)-1]
    return server_ip

def get_client_ip(client_name,config_hashmap):
    """ Gives the client ip given the client name
    Args:
        client_name: name of the client as in config file.
                     example: client_vm1
        config_hashmap: the config file dictionary generated
                        while parsing.
    Returns:
        ip address of the given client
    Example:
        get_client_ip("client_vm1",config_hashmap)
    """
    index = client_name[9:]
    client_ip = config_hashmap['clients'][int(index)-1]
    return client_ip

def get_server_ip_list(config_hashmap):
    """ Gives the list of all server ip
    Args:
        config_hashmap: the config file dictionary generated
                        while parsing.
    Returns:
        list of all server ip address
    Example:
        get_server_ip_list(config_hashmap)
    """
    server_ip_list = config_hashmap['servers']
    return server_ip_list

def get_client_ip_list(config_hashmap):
    """ Gives the list of all client ip
    Args:
        config_hashmap: the config file dictionary generated
                        while parsing.
    Returns:
        list of all client ip address
    Example:
        get_client_ip_list(config_hashmap)
    """
    client_ip_list = config_hashmap['clients']
    return client_ip_list

def get_brick_root_list(server_name,config_hashmap):
    """ Returns the list of brick root given the server name
    Args:
        server_name: name of the server as in config file.
                     example: server_vm1
        config_hashmap: the config file dictionary generated
                        while parsing.
    Returns:
        ilist of brick root of the given server
    Example:
        get_brick_root_list("server_vm1",config_hashmap)
    """
    server_ip = get_server_ip(server_name,config_hashmap)
    brick_root_list = config_hashmap['servers_info'][server_ip]['brick_root']
    return brick_root_list

def volume_create_force_option(config_hashmap):
    """ Returns the flag for volume_create_force option
    Args:
        config_hashmap: the config file dictionary generated
                        while parsing.
    Returns:
        flag value(True/False) for volume_create_force option
    Example:
        volume_create_force_option(config_hashmap)
    """
    volume_create_force = config_hashmap['gluster']["volume_create_force"]
    return volume_create_force




