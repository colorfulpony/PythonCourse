import requests
import time

def get_weather_forecast(city_name, API_key="bb5bdb3567320875293364bf16185e0f"):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={API_key}&units=metric"
    r = requests.get(url)
    content = r.json()
    weather_by_time = content['list']

    with open("data.txt", "a") as file:
        for weather in weather_by_time:
            file.write(f"\n{city_name}, {weather['dt_txt']}, {weather['main']['temp']}, {weather['weather'][0]['description']}")

get_weather_forecast("London")


#       {
#          "dt":1647356400,
#          "main":{
#             "temp":8.13,
#             "feels_like":4.61,
#             "temp_min":7.42,
#             "temp_max":8.13,
#             "pressure":1015,
#             "sea_level":1015,
#             "grnd_level":1014,
#             "humidity":79,
#             "temp_kf":0.71
#          },
#          "weather":[
#             {
#                "id":500,
#                "main":"Rain",
#                "description":"light rain",
#                "icon":"10d"
#             }
#          ],
#          "clouds":{
#             "all":95
#          },
#          "wind":{
#             "speed":6.78,
#             "deg":184,
#             "gust":12.14
#          },
#          "visibility":10000,
#          "pop":0.34,
#          "rain":{
#             "3h":0.27
#          },
#          "sys":{
#             "pod":"d"
#          },
#          "dt_txt":"2022-03-15 15:00:00"
#       }