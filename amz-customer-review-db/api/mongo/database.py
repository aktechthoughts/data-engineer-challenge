"""
This is the main class which handles requests for mongodb database.
"""

import json
from pymongo import MongoClient, errors
from api.exception import api_execption
import logging
import pandas as pd
import subprocess
from bson.json_util import dumps


class Database:
    
    mongoclient = None
    tableconfig = None
    
    def __init__(self, config,tcon ):
        """
        Initialize Metadata Config
        :param config: config file
        """
        
        # use a try-except indentation to catch MongoClient() errors
        try:
            # try to instantiate a client instance
            self.mongoclient = MongoClient(
                host = [ str(config.host) + ":" + str(config.port) ],
                serverSelectionTimeoutMS = config.timeout, # 3 second timeout
                username = config.username,
                password = config.password,
            )

            # print the version of MongoDB server if connection successful
            print ("server version:", self.mongoclient.server_info()["version"])

        
        except errors.ServerSelectionTimeoutError as err:
            # set the client and DB name list to 'None' and `[]` if exception
            self.mongoclient = None
        
            # catch pymongo.errors.ServerSelectionTimeoutError
            print ("pymongo ERROR:", err)

        self.tableconfig = tcon

    """
    The method adds records in the table given by  - tablename.
    It fetches data from the file - filename
    The configuration of the file is given in - tcon
    """
    def add_records_in_table(self,tablename,filename):
        self.tsv_to_json(filename)
        subprocess.call(['mongodb/mongoimport.sh',tablename]) 


    def tsv_to_json(self,filename):
        col_list = [attrib['name'] for attrib in self.tableconfig.attributes]
        df = pd.read_csv(filename, names=col_list, header=None,sep='\t',low_memory=False)
        df = df.loc[df['marketplace'].str.len() == 2]
        df.to_json("input/temp.json",orient='records') 
        
        

    def get_product_count(self,tablename):
        agg_string = ".aggregate([{'$group': {'_id':{'product_id':'$product_id'}, 'count':{'$sum':1}}}])"

        db = "self.mongoclient.admin."
        res = eval(str(db)+tablename+str(agg_string))


        json_object = json.dumps(dumps(res))

        with open("input/temp.json", "w") as outfile: 
            json.dump(json_object, outfile,indent=2)


        
        
        
        

