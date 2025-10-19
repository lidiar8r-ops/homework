import  json
import requests
from dotenv import load_dotenv

url = 'https://api.apilayer.com/exchangerates_data/convert'
payload = {
    "amount": "1200",
    "from": "EUR",
    "to": "RUB"
}

# Загрузка переменных из .env-файла
load_dotenv()
headers= {
  "apikey": API_KEY
}

response = requests.get(url, headers=headers, data = payload)

def get_currency_exchange(transaction: dict)-> float:
    """
    принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях, тип данных —float.
    Если транзакция была в USD или EUR, происходит обращение к внешнему API для получения текущего курса валют и
    конвертации суммы операции в рубли.
    :param transaction: транзакция
    :return: сумма транзакции
    """
    response = requests.get(url, 'base=RUB&symbols=EUR,USD')
    if response.status_code == 200:
        all_repositoris = [repo["full_name"] for repo in response.json()]
    else:
        all_repositoris = 0

    return all_repositoris


