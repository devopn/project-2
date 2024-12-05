from flask import Flask, render_template, request
from config.config import load_config, Config

import src.services.city as city

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
    data = city.get_city_info(start, config)
    print(data)
    result = 'Good'

    return render_template('result.html', start=start, end=end, result=result)

if __name__ == '__main__':
    config: Config = load_config()
    app.run()