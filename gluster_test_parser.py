import yaml
import argparse


class Parser():

    @staticmethod
    def generate_config_hashmap(filepath):
        """Function to generate hashmap"""
        try:
            configfd = open(filepath,'r')
            config_hashmap = yaml.load(configfd, Loader=yaml.FullLoader)
            configfd.close()
            return config_hashmap
        except Exception as err:
            print(err)
            return None

    



