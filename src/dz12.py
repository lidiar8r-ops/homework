import os
import  json


def get_weather(city: str):
    with open("..\\data\\weather.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        day_temperature = [value for value in  data[city].values() ]
        #print(day_temperature)
        #with open(f"..\\data\\weather_{city}.json", "w", encoding="utf-8") as f:
        data_city = { f"{city}": f"{sum(day_temperature) / 7}"}
        with open("..\\data\\weather_city.json", "w", encoding="utf-8") as f:
            json.dump(data_city, f, ensure_ascii=False, indent=4)
        return sum(day_temperature) / 7




print(get_weather("Moscow"))