import json


"""
This class is used to store the Database configuration from the file.
"""
class DBConfigService(object):

    def __init__(self,config,dbtype='mysql'):
        # store parameters
        self.config = config

        # open system config file
        with open(config) as data_file:
            params = json.load(data_file)


            self.host = params[dbtype]["host"]
            self.port = params[dbtype]["port"]
            self.dbname = params[dbtype]["dbname"]
            self.username = params[dbtype]["username"]
            self.password = params[dbtype]["password"]

            if dbtype == 'mongo':
                self.timeout = params["mongo"]["timeout"]


"""
This class is used to store the Tables configuration from the file.
"""

class TableConfigService(object):

    def __init__(self, config):
        # store parameters
        self.config = config

        # open system config file
        with open(config) as data_file:
            params = json.load(data_file)

        self.filenames = params["filenames"]
        self.num_of_attr = params["num_of_attr"]
        self.attributes = params["attibutes"]

    def get_file_location(self,filename):
        return "https://s3.amazonaws.com/amazon-reviews-pds/tsv/amazon_reviews_us_" + \
                str(filename) + \
                ".tsv.gz"    

