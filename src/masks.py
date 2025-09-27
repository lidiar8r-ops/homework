from typing import Union


def get_mask_card_number(numbers: int) -> Union[str]:
    """Функция маскировки номера банковской карты в виде XXXX XX** **** XXXX, где
    X — это цифра номера.
    :rtype: Union[str]"""
    # проверка на тип
    for arg in [numbers]:
        if not isinstance(arg, int):
            raise TypeError('Ошибка типа данных')

    # проверка на пустую строку
    if numbers == 0 or numbers == None:
        raise TypeError('Номер карты не может быть пустым')

    str_num = str(numbers)

    # проверка на корректность длины
    if len(str_num) != 16:
        raise ValueError('Длина номера карты не равна 16')

    return f"{str_num[0:4]} {str_num[4:6]}** **** {str_num[-4:]}"


def get_mask_account(numbers: int) -> Union[str]:
    """Функция маскировки номера банковского счета, Номер счета замаскирован
    и отображается в формате **XXXX, где X — это цифра номера"""

    str_num = str(numbers)
    return f"**{str_num[-4:]}"


# print(get_mask_card_number(7000792289606361))
# print(get_mask_account(73654108430135874305))
