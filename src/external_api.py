import json.decoder
import logging
import os

import requests
from dotenv import load_dotenv

# Получаем директорию текущего файла (т.е. папку src)
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
# Формируем абсолютный путь к папке log (которая находится на уровень выше)
LOG_DIR = os.path.join(CURRENT_DIR, "..", "logs")
log_file_path = os.path.join(LOG_DIR, "external_api.log")

# Настройка логирования
logger_external_api = logging.getLogger("external_api")
file_handler_external_api = logging.FileHandler(log_file_path, "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler_external_api.setFormatter(file_formatter)
logger_external_api.addHandler(file_handler_external_api)
logger_external_api.setLevel(logging.DEBUG)


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
        carrency_code = transaction.get("operationAmount", {}).get("currency", {}).get("code", "")
        if carrency_code == "RUB":
            return float(transaction.get("operationAmount", {}).get("amount", 0))
        else:
            amount_transaction = transaction.get("operationAmount", {}).get("amount", 0)
            if not amount_transaction == 0:
                params_load = {"amount": amount_transaction, "from": carrency_code, "to": "RUB"}
                response = requests.get(url=url, params=params_load, headers=headers)
                # print(response)
                if response.status_code == 200:
                    try:
                        return float(response.json()["result"])
                    except json.decoder.JSONDecodeError as e:
                        raise (e)
                else:
                    print(f" Ошибка статус - код: {str(response.status_code)}")
                    return 0
            else:
                return 0
    except Exception as e:
        raise (e)
