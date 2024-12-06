from flask import Flask, render_template, request
from config.config import load_config, Config
from src.services.weather import get_daily_weather
from src.services.city import get_city_info
from src.models.Weather import Weather

config:Config


app = Flask(__name__,
            static_folder='src/static',
            template_folder='src/templates')



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check_weather', methods=['GET'])
def get_weather():
    return render_template('form.html')

@app.route('/check-weather', methods=['POST'])
def check_weather():
    try:
        start = request.form['start']
        end = request.form['end']
    except KeyError:
        return render_template('error.html', error='Неверные данные')
    # try:
    #     city1_code, city2_code = get_city_info(start, config), get_city_info(end, config)
    #     city1_weather, city2_weather = get_daily_weather(city1_code['key'], config), get_daily_weather(city2_code['key'], config)
    # except Exception as e:
    #     return render_template('error.html', error=str(e))
    
    city1_weather = [{'date': '2024-12-06T07:00:00+03:00', 'max_temp': -5.1, 'min_temp': -5.9, 'humidity': 80, 'wind_speed': 13.0, 'rain_probability': 0}, {'date': '2024-12-07T07:00:00+03:00', 'max_temp': -2.0, 'min_temp': -2.9, 'humidity': 87, 'wind_speed': 7.4, 'rain_probability': 0}, {'date': '2024-12-08T07:00:00+03:00', 'max_temp': -1.1, 'min_temp': -2.4, 'humidity': 89, 'wind_speed': 16.7, 'rain_probability': 0}, {'date': '2024-12-09T07:00:00+03:00', 'max_temp': -0.4, 'min_temp': -6.8, 'humidity': 88, 'wind_speed': 11.1, 'rain_probability': 0}, {'date': '2024-12-10T07:00:00+03:00', 'max_temp': -3.1, 'min_temp': -5.5, 'humidity': 78, 'wind_speed': 11.1, 'rain_probability': 0}]
    city2_weather = [{'date': '2024-12-06T07:00:00+03:00', 'max_temp': -2.2, 'min_temp': -3.7, 'humidity': 75, 'wind_speed': 14.8, 'rain_probability': 0}, {'date': '2024-12-07T07:00:00+03:00', 'max_temp': -1.5, 'min_temp': -4.0, 'humidity': 81, 'wind_speed': 11.1, 'rain_probability': 0}, {'date': '2024-12-08T07:00:00+03:00', 'max_temp': -0.6, 'min_temp': -2.4, 'humidity': 76, 'wind_speed': 20.4, 'rain_probability': 5}, {'date': '2024-12-09T07:00:00+03:00', 'max_temp': 0.7, 'min_temp': -0.8, 'humidity': 83, 'wind_speed': 14.8, 'rain_probability': 1}, {'date': '2024-12-10T07:00:00+03:00', 'max_temp': 0.7, 'min_temp': -5.4, 'humidity': 86, 'wind_speed': 11.1, 'rain_probability': 25}]
    city1_weather = [Weather(**item) for item in city1_weather]
    city2_weather = [Weather(**item) for item in city2_weather]
    
    result1 = any([item.is_bad() for item in city1_weather])
    result2 = any([item.is_bad() for item in city2_weather])

    

    return render_template('result.html', start=start, end=end,city1_weather=city1_weather, city2_weather=city2_weather, result=result1 or result2)

if __name__ == '__main__':
    config: Config = load_config()
    app.run()