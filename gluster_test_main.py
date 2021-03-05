from gluster_test_parser import (generate_config_hashmap,get_server_ip_list,
                                get_client_ip_list,get_server_ip,get_client_ip,
                                get_brick_root_list,volume_create_force_option)

def main():
    """Function to call the config file parse library"""
    config_hashmap = generate_config_hashmap()
    #print(config_hashmap)
    server_ip_list = get_server_ip_list(config_hashmap)
    client_ip_list = get_client_ip_list(config_hashmap)
    server_ip = get_server_ip("server_vm1",config_hashmap)
    client_ip = get_client_ip("client_vm1",config_hashmap)
    brick_root_list = get_brick_root_list("client_vm1",config_hashmap)
    volume_create_force = volume_create_force_option(config_hashmap)
    #print(server_ip_list)
    #print(client_ip_list)
    #print(server_ip)
    #print(client_ip)
    #print(brick_root)
    #print(volume_create_force)


if __name__ == '__main__':
    main()
