from gluster_params_handler import ParamsHandler
import argparse

def pars_args():
        """Parse arguments with argparse module
        """
        
        parser = argparse.ArgumentParser(
            description='Create config hashmap based on config file')
        parser.add_argument("-c", "--config",
                            help="Config file(s) to read.",
                            action="store", dest="config_file",
                            default=None)
        return parser.parse_args()


def main():

    args = pars_args()
    
    if(args.config_file):
        ParamsHandler.get_config_hashmap(args.config_file)
        
    #Below commands are for testing. Can be removed later.    
    """
    server_ip_list = ParamsHandler.get_server_ip_list()
    client_ip_list = ParamsHandler.get_client_ip_list()
    server_ip = ParamsHandler.get_server_ip("server_vm1")
    client_ip = ParamsHandler.get_client_ip("client_vm1")
    brick_root_list = ParamsHandler.get_brick_root_list("client_vm1")
    volume_create_force = ParamsHandler.volume_create_force_option()
    print(server_ip_list)
    print(client_ip_list)
    print(server_ip)
    print(client_ip)
    print(brick_root_list)
    print(volume_create_force)
    """

if __name__ == '__main__':
    main()
