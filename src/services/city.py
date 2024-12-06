import requests
from config.config import Config

def get_city_info(city_name: str, config:Config) -> dict:
    base_url = 'http://dataservice.accuweather.com/locations/v1/cities/search'
    query = {
        'apikey': config.accuweather.daily_api,
        'q': city_name
    }
    
    response = requests.get(base_url, params=query)
    if response.status_code != 200:
        raise Exception('Проблемы с AccuWeather: ' + str(response.status_code))
    return {
        'key': response.json()[0]['Key'],
        'name': response.json()[0]['LocalizedName'],
        'lon': response.json()[0]['GeoPosition']['Longitude'],
        'lat': response.json()[0]['GeoPosition']['Latitude']
    }