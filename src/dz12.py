import datetime
import  json

import requests


def get_avg_weather(city: str):
    """Получение средней температура по городу city"""
    try:
        with open("..\\data\\weather.json", "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                print("Ошибка обработки JSON файла")
                return False
    except FileNotFoundError:
        print("Файл не найден")
        return False

    if len(data[city].values()) == 0:
        avg_temperature = 0
    else:
        avg_temperature = round(sum(data[city].values()) / len(data[city].values()), 2)

    data_city = { city:
        {
            "Average temperature": avg_temperature
        }
    }
    with open("..\\data\\weather_city.json", "w", encoding="utf-8") as f:
        json.dump(data_city, f, ensure_ascii=False, indent=4)
    return True


def get_days_between_dates(date1, date2: str) -> int:
    """ Получение дней между датами"""
    date_dt_1 = datetime.datetime.strptime(date1, "%d.%m.%Y")
    date_dt_2 = datetime.datetime.strptime(date2, "%d.%m.%Y")
    return (date_dt_2 - date_dt_1).days


def get_github_repos(username: str) -> list[str]:
    """ Получение репозиториев пользователя"""
    response = requests.get('https://api.github.com/users/{username}/repos'.format(username=username))
    if response.status_code == 200:
        all_repositoris = [repo["full_name"] for repo in  response.json()]
    else:
       all_repositoris = 0

    return all_repositoris


def get_users_repos() -> None:
    """ Получение репозиториев пользователя"""
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    print(response)
    if response.status_code == 200:
        all_repositoris = [repo["full_name"] for repo in  response.json()]
    else:
       all_repositoris = 0

    return all_repositoris


# print(get_avg_weather("Moscow"))
#
# print(get_days_between_dates("01.01.2022", "31.01.2022"))
#
# repos = get_github_repos('octocat')
# print(repos)


print(get_users_repos())