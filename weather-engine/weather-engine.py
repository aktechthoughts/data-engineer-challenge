"""
This file is the entry point for the application.
"""
import json
from weather.config import config_service
from weather.climateapi import climateapi


def get_weather():
    config = config_service.ConfigService(config='config.json')
    api = climateapi.Climate(config)

    res = api.get_weather_by_city_post_code(post=91056,country='de')
    # res = api.get_weather_by_city_location(long=38.12,lat=2000)
    # res = api.get_weather_by_city_name(name='Raleigh')
    # res = api.get_weather_by_city_id(citi_id=8953360)

    print(json.dumps(res, indent=4, sort_keys=True))

if __name__ == "__main__":
    get_weather();
    
