class Weather:
    def __init__(self, temp, humidity, wind_speed, rain_probability):
        self.temp = temp
        self.humidity = humidity
        self.wind_speed = wind_speed
        self.rain_probability = rain_probability

    def is_bad(self):
        return (
            self.temp < 0 or
            self.temp > 35 or
            self.wind_speed > 50 or
            self.rain_probability > 70 or 
            self.humidity > 90 or 
            self.humidity < 30
        )
    