import yaml
import argparse


class Parser():

    def __init__(self):
        self.generate_config_hashmap()

    def open_file(self,filename):
        """Function opens file and returns file descriptor."""
        f = open(filename,'r')
        return f

    def load_yaml(self,filename):
        """Function to read config file"""
        configfd = self.open_file(filename)
        if configfd:
            config = yaml.load(configfd, Loader=yaml.FullLoader)
            return config
        return None

    def handle_config(self,config_file):
        """Load user configuration files"""

        if config_file:
            ret = self.load_yaml(config_file)
            return ret

        return False

    def parse_args(self):
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

    def generate_config_hashmap(self):
        """Function to generate hashmap"""

        args = self.parse_args()

        if args.config_file:
            config_hashmap = self.handle_config(args.config_file)
            self.config_hashmap = config_hashmap

    def get_server_ip(self,server_name):
        """ Gives the server ip given the server name
        Args:
            server_name: name of the server as in config file.
                         example: server_vm1
        Returns:
            ip address of the given server
        Example:
            get_server_ip("server_vm1")
        """
        index = server_name[9:]
        server_ip = self.config_hashmap['servers'][int(index)-1]
        return server_ip

    def get_client_ip(self,client_name):
        """ Gives the client ip given the client name
        Args:
            client_name: name of the client as in config file.
                         example: client_vm1
        Returns:
            ip address of the given client
        Example:
            get_client_ip("client_vm1")
        """
        index = client_name[9:]
        client_ip = self.config_hashmap['clients'][int(index)-1]
        return client_ip

    def get_server_ip_list(self):
        """ Gives the list of all server ip
        Returns:
            list of all server ip address
        """
        server_ip_list = self.config_hashmap['servers']
        return server_ip_list

    def get_client_ip_list(self):
        """ Gives the list of all client ip
        Returns:
            list of all client ip address
        """
        client_ip_list = self.config_hashmap['clients']
        return client_ip_list

    def get_brick_root_list(self,server_name):
        """ Returns the list of brick root given the server name
        Args:
            server_name: name of the server as in config file.
                         example: server_vm1
        Returns:
            ilist of brick root of the given server
        Example:
            get_brick_root_list("server_vm1")
        """
        server_ip = self.get_server_ip(server_name)
        servers_info = self.config_hashmap['servers_info']
        brick_root_list = servers_info[server_ip]['brick_root']
        return brick_root_list

    def volume_create_force_option(self):
        """ Returns the flag for volume_create_force option
        Returns:
            flag value(True/False) for volume_create_force option
        """
        gluster_info = self.config_hashmap['gluster']
        volume_create_force = gluster_info['volume_create_force']
        return volume_create_force




