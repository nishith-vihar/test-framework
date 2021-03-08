from gluster_test_parser import Parser

def main():
    parser = Parser()
    server_ip_list = parser.get_server_ip_list()
    client_ip_list = parser.get_client_ip_list()
    server_ip = parser.get_server_ip("server_vm1")
    client_ip = parser.get_client_ip("client_vm1")
    brick_root_list = parser.get_brick_root_list("client_vm1")
    volume_create_force = parser.volume_create_force_option()
    print(server_ip_list)
    print(client_ip_list)
    print(server_ip)
    print(client_ip)
    print(brick_root_list)
    print(volume_create_force)

if __name__ == '__main__':
    main()
