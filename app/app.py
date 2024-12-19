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
    try:
        city1_code, city2_code = get_city_info(start, config), get_city_info(end, config)
        city1_weather = get_daily_weather(city1_code['key'], config)
        city2_weather = get_daily_weather(city2_code['key'], config)
    except Exception as e:
        return render_template('error.html', error=str(e))
    
    try:
        city1_weather = [Weather(**item) for item in city1_weather]
        city2_weather = [Weather(**item) for item in city2_weather]
    except Exception as e:
        return render_template('error.html', error='Error with API')
    
    result = any([item.is_bad() for item in city1_weather + city2_weather])
    return render_template('result.html', start=start, end=end,
                            city1_weather=city1_weather, city2_weather=city2_weather,
                            result=result)

@app.errorhandler(404)
def error_handler(e):
    return render_template('error.html', error='Page not found')

@app.errorhandler(500)
def error_handler(e):
    return render_template('error.html', error='Internal server error')

@app.errorhandler(503)
def error_handler(e):
    return render_template('error.html', error='Service unavailable')

if __name__ == '__main__':
    config: Config = load_config()
    app.run(host='0.0.0.0', port=5000, debug=False)