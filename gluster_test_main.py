from gluster_test_parser import generate_config_hashmap

def main():
    """Function to call the config file parse library"""
    config_hashmap = generate_config_hashmap()
    print(config_hashmap)


if __name__ == '__main__':
    main()
