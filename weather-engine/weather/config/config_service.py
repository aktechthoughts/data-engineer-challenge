import json


"""
This class is used to store the configuration from the file.
"""
class ConfigService(object):

    def __init__(self, config):
        # store parameters
        self.config = config

        # open system config file
        with open(config) as data_file:
            params = json.load(data_file)

        self.url = params["url"]
        self.emails = params["email"]
        self.key = params["key"]
        self.name = params["Author"]
        self.log_name = params["log_name"]


