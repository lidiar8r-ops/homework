import json.decoder
import os

import requests
from dotenv import load_dotenv

# Загрузка переменных из .env-файла,3
load_dotenv()
headers = {"apikey": os.getenv("API_KEY")}

url = "https://api.apilayer.com/exchangerates_data/convert"


def get_currency_exchange(transaction: dict) -> float:
    """
    принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях, тип данных —float.
    Если транзакция была в USD или EUR, происходит обращение к внешнему API для получения текущего курса валют и
    конвертации суммы операции в рубли.
    :param transaction: транзакция
    :return: сумма транзакции
    """

    try:
        if transaction.get("operationAmount", {}).get("currency", {}).get("code", {}) == "RUB":
            return float(transaction.get("operationAmount", {}).get("amount", 0))
        else:
            amount_transaction = transaction.get("operationAmount", {}).get("amount", 0)
            if not amount_transaction == 0:
                params_load = {"amount": amount_transaction, "from": "EUR", "to": "RUB"}
                response = requests.get(url=url, params=params_load, headers=headers)
                print(response)
                if response.status_code == 200:
                    try:
                        return float(response.json()["result"])
                    except json.decoder.JSONDecodeError as e:
                        raise (e)
                else:
                    raise (response.status_code)
            else:
                return 0
    except Exception as e:
        raise (e)


# params_load_p = {
#     "id": 41428829,
#     "state": "EXECUTED",
#     "date": "2019-07-03T18:35:29.512364",
#     "operationAmount": {
#       "amount": "100",
#       "currency": {
#         "name": "USD",
#         "code": "USD"
#       }
#     },
#     "description": "Перевод организации",
#     "from": "MasterCard 7158300734726758",
#     "to": "Счет 35383033474447895560"
#   }
# print(get_currency_exchange(params_load_p))
