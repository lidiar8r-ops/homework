import logging
import os
import re

import pandas as pd
from typing import Any, Dict, List


# Получаем директорию текущего файла (т.е. папку src)
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
# Формируем абсолютный путь к папке log (которая находится на уровень выше)
LOG_DIR = os.path.join(CURRENT_DIR, "..", "logs")
log_file_path = os.path.join(LOG_DIR, "geneators.log")

# Настройка логирования
logger_get_scv_xls = logging.getLogger("get_scv_xls")
file_handler_get_scv_xls = logging.FileHandler(log_file_path, "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler_get_scv_xls.setFormatter(file_formatter)
logger_get_scv_xls.addHandler(file_handler_get_scv_xls)
logger_get_scv_xls.setLevel(logging.DEBUG)


def get_csv_xlsx_reader_transaction(path_filename: str) -> list:
    """
    Функция пытается прочитать файл CSV или Excel, преобразовать содержимое в словарь и сформировать список словарей
    с транзакциями.
    :param path_filename: путь к файлу CSV или XLX, XLSX
    :return: словарь с транзакциями
    """
    result_list: List[Dict[str, Any]] = []
    try:
        # Проверка существования файла
        if not os.path.isfile(path_filename):
            logger_get_scv_xls.error(f"Не найден файл {path_filename}")
            return result_list

        # Проверка расширения файла
        extension = os.path.splitext(path_filename)[1].upper()
        pattern = r"\.(XLS|XLSX|CSV)"

        if not re.search(pattern, extension, re.IGNORECASE):
            print(f"Файл {os.path.basename(path_filename)} не соответствует расширению CSV или XLSX,XLX")
            return result_list

        # Выбор способа открытия файла
        if extension == ".CSV":
            df = pd.read_csv(path_filename, delimiter=";")
        else:
            df = pd.read_excel(path_filename)

        logger_get_scv_xls.info(f"Чтение данных из файла {os.path.basename(path_filename)} ")

        # Прверим, что все колонки присутствуют
        index_column = [
            "id",
            "state",
            "date",
            "amount",
            "currency_name",
            "currency_code",
            "from",
            "to",
            "description",
        ]
        if len(df.columns) != len(index_column):
            logger_get_scv_xls.error(f"Ошибка в данных, отсутствует колонка {set(index_column) - set(df.columns)}")
            return result_list

        # Преобразование прочитанного в словарь
        dict_df_get = df.to_dict(orient="records")
        logger_get_scv_xls.info("Преобразование прочитанного в словарь")

        # Если файл только с заголовками, а данных нет
        if len(dict_df_get) == 0:
            logger_get_scv_xls.error(f"Нет информации в файле {path_filename} ")
            return result_list

        # Обработка полученных данных
        for values in dict_df_get:
            result_list.append(
                {
                    "id": values["id"],
                    "state": values["state"],
                    "date": values["date"],
                    "operationAmount": {
                        "amount": values["amount"],
                        "currency": {"name": values["currency_name"], "code": values["currency_code"]},
                    },
                    "description": values["description"],
                    "from": values["from"],
                    "to": values["to"],
                }
            )

        logger_get_scv_xls.info("Сформирован список словарей с транзакциями")
        return result_list

    except ValueError as e:
        logger_get_scv_xls.error(e)
        return result_list

    except Exception as ex:
        logger_get_scv_xls.error(f"Необработанная ошибка: {ex}")
        return result_list
