"""
This is the main class which handles API requests.
"""

import json
import requests
from weather.exception import api_execption
import logging

class Climate:
    
    url =''
    payload = {'key': ''}

    def __init__(self, config ):
        """
        Initialize Metadata Config
        :param config: config file
        """
        self.url = config.url
        self.payload['key'] = config.key
        logging.basicConfig(filename=config.log_name,level=logging.DEBUG)

    """
    The method fetches the weather of city given by lattitue and longitude.
    This also validates the location of the city and raises exception. 
    """
    def get_weather_by_city_location(self,long,lat):

        if long not in range(-180,180) and lat not in range(-90,90):
            logging.debug('The location ({},{}) is not correct.'.format(lat,long))            
            raise api_execption.LocationException('The location ({},{}) is not correct.'.format(lat,long))

        self.payload['lon'] = long
        self.payload['lat'] = lat
        

        resp = requests.get(self.url, params=self.payload)
        if resp.status_code != 200:
            logging.debug('The API returnned {} code.'.format(resp.status_code))
            raise api_execption.ApiException('The API returnned {} code.'.format(resp.status_code))
        else:
            parsed = json.loads(resp.content)
            return parsed
            logging.info('The API get_weather_by_city_location has run successfully')



    """
    The method fetches the weather of city given by name
    state and country are optional parameters.
    """

    def get_weather_by_city_name(self,name,state='',country=''):
        self.payload['city'] = name
        self.payload['country'] = country
        self.payload['state'] = state
        

        resp = requests.get(self.url, params=self.payload)
        if resp.status_code != 200:
            logging.debug('The API returnned {} code.'.format(resp.status_code))            
            raise api_execption.ApiException('The API returnned {} code.'.format(resp.status_code))
        else:
            parsed = json.loads(resp.content)
            return parsed
            logging.info('The API get_weather_by_city_name has run successfully')        


    """
    The method fetches the weather of city given by citi_id
    citi_id is mandatory parameter.
    """

    def get_weather_by_city_id(self,citi_id):
        self.payload['city_id'] = citi_id

        resp = requests.get(self.url, params=self.payload)
        if resp.status_code != 200:
            logging.debug('The API returnned {} code.'.format(resp.status_code))            
            raise api_execption.ApiException('The API returnned {} code.'.format(resp.status_code))
        else:
            parsed = json.loads(resp.content)
            return parsed
            logging.info('The API get_weather_by_city_id has run successfully')        

    """
    The method fetches the weather of city given by post code.
    country code is optional and default country code is 'US'
    """
    def get_weather_by_city_post_code(self,post,country='US'):
        self.payload['postal_code'] = post
        self.payload['country'] = country
        

        resp = requests.get(self.url, params=self.payload)
        if resp.status_code != 200:
            logging.debug('The API returnned {} code.'.format(resp.status_code))            
            raise api_execption.ApiException('The API returnned {} code.'.format(resp.status_code))
        else:
            parsed = json.loads(resp.content)
            return parsed
            logging.info('The API get_weather_by_post_code has run successfully')                    
