import requests 

def get_daily_weather(code, config):
    base_url = f'http://dataservice.accuweather.com/forecasts/v1/daily/5day/296543/{code}'
    query = {
        'apikey': config.accuweather.daily_api,
        'metric':True,
        'details':True
    }

    response = requests.get(base_url, params=query)
    if response.status_code == 200:
        result = [
            {} for day in response.json()['DailyForecasts']
        ]
    else:
        return None