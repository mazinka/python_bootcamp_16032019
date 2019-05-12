import urllib.request
import json
import requests
import sys

print(__name__)
def get_location_id(location_name):
    resp = requests.get(f'https://www.metaweather.com/api/location/search/?query={location_name}')
    print (resp.json())
    return resp.json()[0] ['woeid']


def get_location_weather(location_id):
    resp = requests.get(f'https://www.metaweather.com/api/location/{location_id}/')
    return resp.json()['consolidated_weather'][0]


def print_weather(weather, location_name):
    description ='''
    pogoda w {location_name}:
    temperatura: {weather["the_temp"]}
    ciśnienie: {weather["air_pressure"]}
    '''

    print(description)

if __name__ == '__main__':
    if len(sys.argv) <2:
        location_name ="warsaw"
    else:
        location_name =sys.argv[1]


    location_id = get_location_id(location_name)
    weather = get_location_weather(location_id)
    print (weather, location_name)

