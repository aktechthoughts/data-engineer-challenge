# Why I choose weatherbit.io API
I wanted to choose blablacar api or stormglass api. But, blabla didn't give me immediate access to apikey. The documentation of stormglass api was not working.

The weatherbit.io gave me access key immediately and the documentation was very neat. 

# What is this application

weather api is a wrapper to https://weatherbit.io/v2.0/current 
this exposes four end points 

* **get_weather_by_city_post_code** 
    This api takes post code as input and returns json string.
* **get_weather_by_city_location** 
    This api takes city location ( latitude & longitude) as input and returns json string. Also, returns LocationException if the latitude & longitude is correct.
* **get_weather_by_city_name** 
    This api takes name of the city as input and returns json string. State and Country are optional parameters.
* **get_weather_by_city_id** 
    This api takes citi_id as input and returns climate information in json format.

The application is fully configureale and config.json can be modified to add key & log file.

```

{
    "url":"https://api.weatherbit.io/v2.0/current",
    "key":"61726bebc7ef4b3e91d7b91ec42966cd",
    "log_name":"weather.log",
    "Author":"Abhishek Kumar",
    "email":"abhishek_ku@yahoo.com"
}

```
# How to Build

Unit test is integrated the build.sh will run the testcases in a dokcer environment.
Execute below to trigger a new build.
```
sh build.sh
```
The result of the unit tests is available in tests-results/result.xml - This is junit file and it can be converted into more readable html format.

# How to Execute

The api is used in the weather-engine.py and it can be checked using it will generate a log file - weather.log

```
python weather-engine.py
```

The application can be extended to include Jenkinsfile to provide CI/CD capabilities.
