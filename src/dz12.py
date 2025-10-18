import datetime
import  json
import logging

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


logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('..\\logs\\log_dz.log')
file_formatter = logging.Formatter('%(levelname)s: %(name)s: Request Time: %(asctime)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)

def get_users_repos() -> None:
    """ Получение репозиториев пользователя"""
    logger.info(f"Получение данных")
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    # print(response)
    if response.status_code == 200:
        name_file = "..\\data\\users.json"
        logger.info(f"запись полученных данных в файл {name_file}")
        with open(name_file, "w", encoding="utf-8") as f:
            json.dump(response.json(), f, ensure_ascii=False, indent=4)

    else:
        logger.error('Ошибка получения данных')

# print(get_avg_weather("Moscow"))
#
# print(get_days_between_dates("01.01.2022", "31.01.2022"))
#
# repos = get_github_repos('octocat')
# print(repos)


print(get_users_repos())