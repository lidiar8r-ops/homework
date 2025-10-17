import datetime
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


def get_days_between_dates(date_1, date_2: str):
    date_dt_1 = datetime.datetime.strptime(date_1, "%d.%m.%Y")
    date_dt_2 = datetime.datetime.strptime(date_2, "%d.%m.%Y")
    return date_dt_2 - date_dt_1




# print(get_weather("Moscow"))
print(get_days_between_dates("01.01.2022", "31.01.2022"))