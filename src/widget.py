from datetime import datetime

import src.masks as masks


def mask_account_card(init_str: str) -> str:
    """
    функция, которая обрабатывает информацию как о картах, так и о счетах и
    возвращает строку с замаскированным номером
    :param init_str: принимает аргумент — строка, содержащая тип и номер карты или счета
    :rtype: str возвращает строку с замаскированным номером
    """
    pozition_symbol = init_str.rfind(" ")

    if pozition_symbol > 0:
        pozition_symbol += 1
        try:
            if "СЧЕТ" in init_str.upper():
                new_str = "Счет " + masks.get_mask_account(int(init_str[5:]))
            else:
                new_str = init_str[: pozition_symbol + 1] + masks.get_mask_card_number(int(init_str[pozition_symbol:]))
        except ValueError as e:
            raise ValueError(e)
        except TypeError as e:
            raise TypeError(e)
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
    formatted_datetime = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f")
    return formatted_datetime.strftime("%d.%m.%Y")


# print(mask_account_card("Maestro1596837868705199"))
# print(mask_account_card("Maestro 1596837833368705199"))
# print(mask_account_card("64686473678894779589"))
# print(mask_account_card("Visa Classic 6ввв831982476737658"))
# print(mask_account_card("Visa Classic "))
# print(mask_account_card("СЧЕТ73654108430135874305"))
# print(mask_account_card("СЧЕТ 73654108430135874305"))
# print(mask_account_card("СЧЕТ"))
# print(mask_account_card("Счет 44473654108430135874305"))
# print(mask_account_card("Счет73654108430135874305"))





# print(mask_account_card('Maestro 1596837868705199'))
# print(mask_account_card('Счет 64686473678894779589'))
# print(mask_account_card('MasterCard 7158300734726758'))
# print(mask_account_card('Visa Classic 6831982476737658'))
# print(mask_account_card('Счет 73654108430135874305'))
# print(get_date("2024-03-11T02:26:18.671407"))
