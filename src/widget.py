from datetime import datetime

import src.masks as masks


def mask_account_card(init_str: str) -> str:
    """
    функция, которая обрабатывает информацию как о картах, так и о счетах и
    возвращает строку с замаскированным номером
    :param init_str: принимает аргумент — строка, содержащая тип и номер карты или счета
    :rtype: str возвращает строку с замаскированным номером
    """
    if init_str == None:
        raise TypeError('Номер счета или карты не может быть пустым')
    try:
        pozition_symbol = init_str.rfind(" ")
    except AttributeError as e:
        raise AttributeError(e)

    if pozition_symbol > 0:
        pozition_symbol += 1
        try:
            if "СЧЕТ" in init_str.upper():
                new_str = "Счет " + masks.get_mask_account(int(init_str[5:]))
            else:
                new_str = init_str[: pozition_symbol + 1] + masks.get_mask_card_number(int(init_str[pozition_symbol:]))
        except ValueError as e:
            raise ValueError(e)
        # except TypeError:
        #     raise TypeError("Некорректный тип данных")
        else:
            return new_str
    else:
        raise ValueError('Некорректный формат данных')


def get_date(date_str: str) -> str:
    """
    функция, которая принимает на вход строку с датой и возвращает строку с датой
    :param date_str: строка с датой в формате "2024-03-11T02:26:18.671407"
    :rtype: str возвращает строку с датой в формате "ДД.ММ.ГГГГ" ("11.03.2024").
    """
    try:
        formatted_datetime = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f")
    except ValueError:
        raise ValueError("Не соответствует формату даты")
    except TypeError:
        raise TypeError("Не соответствует типу даты")
    else:
        return formatted_datetime.strftime("%d.%m.%Y")

#
# from dateutil import parser
# date_string = "20/10/2021"
# try:
#     parser.parse(date_string)
#     print("Дата корректна")
# except ValueError:
#     print("Дата некорректна")

# print(get_date("2024-03-11T02:26:18.671407"))
