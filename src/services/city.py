import requests
from config.config import Config

def get_city_info(city_name: str, config:Config) -> dict:
    base_url = 'http://dataservice.accuweather.com/locations/v1/cities/search'
    query = {
        'apikey': config.accuweather.api_key,
        'q': city_name
    }
    
    response = requests.get(base_url, params=query)
    return {
        'key': response.json()[0]['Key'],
        'name': response.json()[0]['LocalizedName'],
        'lon': response.json()[0]['GeoPosition']['Longitude'],
        'lat': response.json()[0]['GeoPosition']['Latitude']
    }