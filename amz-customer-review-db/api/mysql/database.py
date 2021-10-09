"""
This is the main class which handles requests for mysql database.
"""

import json
import mysql.connector
from api.exception import api_execption
import logging
import pandas as pd

class Database:
    
    mysql = None
    tableconfig = None
    
    def __init__(self, config,tcon ):
        """
        Initialize Metadata Config
        :param config: config file
        """
        
        self.mysql = mysql.connector.connect( 
                host=config.host,
                user=config.username, 
                passwd=config.password,
                database=config.dbname
                )

        self.tableconfig = tcon

    """
    The method adds records in the table given by  - tablename.
    It fetches data from the file - filename
    The configuration of the file is given in - tcon
    """
    
    def add_records_in_table(self,tablename):
        
        f=open("input/temp.json", "r")
        fl =f.readlines()
        mycursor = self.mysql.cursor()


        for i in range(len(fl)):
            sql = "INSERT INTO "+str(tablename)+" (data) VALUES(%s)"
            val = [(fl[i])]
            mycursor.execute(sql, val)

        self.mysql.commit()

    
    def tsv_to_json(self,filename):
        col_list = [attrib['name'] for attrib in self.tableconfig.attributes]
        df = pd.read_csv(filename, names=col_list, header=None,sep='\t')
        df = df.loc[df['marketplace'].str.len() == 2]
        resultJSON = json.loads(df.to_json(orient='index'))

        return resultJSON
        
        
        
        

