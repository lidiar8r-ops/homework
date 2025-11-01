import logging
import os
from datetime import datetime
from typing import Dict, List

# Получаем директорию текущего файла (т.е. папку src)
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
# Формируем абсолютный путь к папке log (которая находится на уровень выше)
LOG_DIR = os.path.join(CURRENT_DIR, "..", "logs")
log_file_path = os.path.join(LOG_DIR, "processing.log")

# Настройка логирования
logger_processing = logging.getLogger("processing")
file_handler_processing = logging.FileHandler(log_file_path, "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler_processing.setFormatter(file_formatter)
logger_processing.addHandler(file_handler_processing)
logger_processing.setLevel(logging.DEBUG)


def filter_by_state(input_list: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """
    функция фильтрует список словарей по значение ключа и возвращает новый список словарей
    :param input_list: список словарей
    :param state:  опционально значение для ключа state, по умолчанию 'EXECUTED'
    :return: list  возвращает список словарей, содержащий только те словари, у которых ключ state соответствует
    указанному значению.
    """
    for current_dict in input_list:
        if "state" not in current_dict.keys():
            logger_processing.error(f"Не найден ключ state для транзакции {current_dict}")
            # raise KeyError("В списке не удалось найти ключ state")

    return [current_dict for current_dict in input_list if current_dict.get("state", {}) == state]


def sort_by_date(input_list: List[Dict], sorting: bool = True) -> List[Dict]:
    """
    Возвращает список словарей, отсортированный по дате.
    :param input_list: список словарей, каждый должен содержать ключ "date" со строкой в формате
    ISO 8601 (YYYY-MM-DDTHH:MM:SSZ)
    :param sorting: порядок сортировки (True — убывание, False — возрастание)
    :return: отсортированный по дате список словарей
    """
    for current_dict in input_list:
        if "date" not in current_dict.keys():
            logger_processing.error(f"Не найден ключ date для транзакции {current_dict}")
            # raise KeyError("В словаре не удалось найти ключ date")

        if not isinstance(current_dict.get("date"), str):
            logger_processing.error(f"Ошибка типа данных в транзакции {current_dict}")
            # raise TypeError("Ошибка типа данных")

        try:
            if datetime.fromisoformat(current_dict.get("date", "").replace("Z", "+00:00")) is None:
                logger_processing.error(
                    f"Не соответствует формату даты {str(current_dict.get('date'))} в транзакции {current_dict}"
                )
        except ValueError:
            logger_processing.error(
                f"Не соответствует формату даты {str(current_dict.get('date'))} в транзакции {current_dict}"
            )
            # raise ValueError("Не соответствует формату даты")

    return sorted(input_list, key=lambda current_dict: current_dict.get("date", ""), reverse=sorting)
