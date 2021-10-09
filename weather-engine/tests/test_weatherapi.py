# -*- coding: utf-8 -*-
"""Test connecting to database"""



import pytest
from weather.config import config_service
from weather.climateapi import climateapi


def test_weather_by_city_post_code():
    config = config_service.ConfigService(config='config.json')
    api = climateapi.Climate(config)
    res = api.get_weather_by_city_post_code(post=91056,country='de')

    assert res['count'] > 0

def test_weather_by_city_location():
    config = config_service.ConfigService(config='config.json')
    api = climateapi.Climate(config)
   
    with pytest.raises(Exception, match=r"The location.*.is not correct."):
        res = api.get_weather_by_city_location(long=38.12,lat=2000)
        
def test_weather_by_city_name():
    config = config_service.ConfigService(config='config.json')
    api = climateapi.Climate(config)
    res = api.get_weather_by_city_name(name='Raleigh')

    assert res['count'] > 0


def test_weather_by_city_id():
    config = config_service.ConfigService(config='config.json')
    api = climateapi.Climate(config)
    res = api.get_weather_by_city_id(citi_id=8953360)

    assert res['count'] > 0

