import logging
import os
from datetime import datetime

import src.masks as masks

# Получаем директорию текущего файла (т.е. папку src)
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
# Формируем абсолютный путь к папке log (которая находится на уровень выше)
LOG_DIR = os.path.join(CURRENT_DIR, "..", "logs")
log_file_path = os.path.join(LOG_DIR, "widget.log")

# Настройка логирования
logger_widget = logging.getLogger("widget")
file_handler_widget = logging.FileHandler(log_file_path, "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler_widget.setFormatter(file_formatter)
logger_widget.addHandler(file_handler_widget)
logger_widget.setLevel(logging.DEBUG)


def mask_account_card(init_str: str) -> str:
    """
    функция, которая обрабатывает информацию как о картах, так и о счетах и
    возвращает строку с замаскированным номером
    :param init_str: принимает аргумент — строка, содержащая тип и номер карты или счета
    :rtype: str возвращает строку с замаскированным номером
    """
    if not init_str:
        # raise TypeError("Номер счета или карты не может быть пустым")
        logger_widget.error("Номер счета или карты не может быть пустым")
        return ""
    try:
        pozition_symbol = init_str.rfind(" ")
    except AttributeError as e:
        logger_widget.error(f"{AttributeError(e)} в {init_str}")
        return ""
        # raise AttributeError(e)

    if pozition_symbol > 0:
        pozition_symbol += 1
        try:
            if "СЧЕТ" in init_str.upper():
                new_str = "Счет " + masks.get_mask_account(int(init_str[5:]))
            else:
                new_str = init_str[: pozition_symbol + 1] + masks.get_mask_card_number(int(init_str[pozition_symbol:]))
        except ValueError as e:
            # raise ValueError(e)
            logger_widget.error(f"{ValueError(e)} в {init_str}")
            return ""
        except TypeError:
            # raise TypeError("Некорректный тип данных")
            logger_widget.error(f"Некорректный тип данных в {init_str}")
            return ""
        else:
            return new_str
    else:
        # raise ValueError("Некорректный формат данных")
        logger_widget.error(f"Некорректный тип данных в {init_str}")
        return ""


def get_date(date_str: str) -> str:
    """
    функция, которая принимает на вход строку с датой и возвращает строку с датой
    :param date_str: строка с датой в формате "2024-03-11T02:26:18.671407"
    :rtype: str возвращает строку с датой в формате "ДД.ММ.ГГГГ" ("11.03.2024").
    """
    try:
        formatted_datetime = datetime.fromisoformat(date_str.replace("Z", "+00:00"))
        # formatted_datetime = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f")
    except ValueError:
        logger_widget.error(f"Не соответствует формату даты {date_str}")
        # raise ValueError("Не соответствует формату даты")
        return ""
    except TypeError:
        logger_widget.error(f"Не соответствует формату даты {date_str}")
        # raise TypeError("Не соответствует типу даты")
        # logger_widget.info("Невозможно декодировать JSON-данные")
        return ""

    return formatted_datetime.strftime("%d.%m.%Y")
