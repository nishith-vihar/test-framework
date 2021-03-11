from gluster_test_parser import Parser

class ParamsHandler:
    
    @classmethod
    def get_config_hashmap(cls,filepath):
        cls.config_hashmap = Parser.generate_config_hashmap(filepath)
    
    @classmethod
    def get_server_ip(cls,server_name):
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
        server_ip = cls.config_hashmap['servers'][int(index)-1]
        return server_ip

    @classmethod
    def get_client_ip(cls,client_name):
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
        client_ip = cls.config_hashmap['clients'][int(index)-1]
        return client_ip

    @classmethod
    def get_server_ip_list(cls):
        """ Gives the list of all server ip
        Returns:
            list of all server ip address
        """
        server_ip_list = cls.config_hashmap['servers']
        return server_ip_list

    @classmethod
    def get_client_ip_list(cls):
        """ Gives the list of all client ip
        Returns:
            list of all client ip address
        """
        client_ip_list = cls.config_hashmap['clients']
        return client_ip_list

    @classmethod
    def get_brick_root_list(cls,server_name):
        """ Returns the list of brick root given the server name
        Args:
            server_name: name of the server as in config file.
                         example: server_vm1
        Returns:
            ilist of brick root of the given server
        Example:
            get_brick_root_list("server_vm1")
        """
        server_ip = cls.get_server_ip(server_name)
        servers_info = cls.config_hashmap['servers_info']
        brick_root_list = servers_info[server_ip]['brick_root']
        return brick_root_list

    @classmethod
    def volume_create_force_option(cls):
        """ Returns the flag for volume_create_force option
        Returns:
            flag value(True/False) for volume_create_force option
        """
        gluster_info = cls.config_hashmap['gluster']
        volume_create_force = gluster_info['volume_create_force']
        return volume_create_force

