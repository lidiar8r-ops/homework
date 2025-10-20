import json
import logging
from typing import Any

logger_utils = logging.getLogger('utils')
file_handler_utils = logging.FileHandler('..\logs\utils.log')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler_utils.setFormatter(file_formatter)
logger_utils.addHandler(file_handler_utils)
logger_utils.setLevel(logging.DEBUG)




def get_list_transaction(path_file: str) -> list[Any]:
    """
    принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях.
    :return:
    :param path_file: путь до JSON-файла
    """
    data = list()
    try:
        with open(path_file, encoding="utf-8") as f:
            data = json.load(f)
        return list(data)
    except json.decoder.JSONDecodeError:
        return []
    except FileNotFoundError:
        return []
