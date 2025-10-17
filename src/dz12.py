import datetime
import  json

import requests


def get_avg_weather(city: str):
    """Получение средней температура по городу city"""
    with open("..\\data\\weather.json", "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            print("Ошибка обработки файла")
        day_temperature = [value for value in  data[city].values() ]

        data_city = { f"{city}": {"Average temperature": f"{sum(day_temperature) / 7}"}}
        with open("..\\data\\weather_city.json", "w", encoding="utf-8") as f:
            json.dump(data_city, f, ensure_ascii=False, indent=4)
        return sum(day_temperature) / 7


def get_days_between_dates(date_1, date_2: str):
    date_dt_1 = datetime.datetime.strptime(date_1, "%d.%m.%Y")
    date_dt_2 = datetime.datetime.strptime(date_2, "%d.%m.%Y")
    return (date_dt_2 - date_dt_1).days

def get_github_repos(username: str) -> list[str]:
    response = requests.get('https://api.github.com/users/{username}/repos'.format(username=username))
    print(response.content)



# print(get_weather("Moscow"))

# print(get_days_between_dates("01.01.2022", "31.01.2022"))

repos = get_github_repos('lidiar8r-ops')
print(repos)