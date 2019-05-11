import openweather
from datetime import datetime

ow = openweather.OpenWeather(cache=False)
stations = ow.find_stations_near(48.10,11.69)

for sta in stations:
    print(sta)

