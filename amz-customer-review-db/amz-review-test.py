"""
This file is the entry point for the application.
"""
import json
from api.config import config_service
from api.exception import api_execption
from api.mysql import database as mysql
from api.mongo import database as mongo
import argparse


def process_mongo_data(tablename,filename):
    tb_config = config_service.TableConfigService(config='config/tcon.json')

    mongo_config = config_service.DBConfigService(config='config/app_config.json',dbtype='mongo')
    mysql_config = config_service.DBConfigService(config='config/app_config.json',dbtype='mysql')

    mongo_db = mongo.Database(config=mongo_config,tcon=tb_config)
    mysql_db = mysql.Database(config=mysql_config,tcon=tb_config)

    mongo_db.add_records_in_table(tablename,filename)    

    mongo_db.get_product_count(tablename)
    mysql_db.add_records_in_table(tablename)


if __name__ == "__main__":
    # process_mysql_data()
    parser = argparse.ArgumentParser()
    parser.add_argument("tname",
                    help="collection name to be loaded.")
    parser.add_argument("fname",
                    help="File name to be loaded in the collection.")                    

    args = parser.parse_args()

    process_mongo_data(args.tname,args.fname)
