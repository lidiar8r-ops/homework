import requests


def get_weather(city: str):
    request = requests.get('https://gismeteo/.../?q=' + city)
    return request


