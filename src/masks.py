from typing import Union


def get_mask_card_number(numbers: int) -> Union[str]:
    """Функция маскировки номера банковской карты в виде XXXX XX** **** XXXX, где
    X — это цифра номера.
    :rtype: Union[str]"""

    str_num = str(numbers)
    return f"{str_num[0:4]} {str_num[4:6]}** **** {str_num[-4:]}"


def get_mask_account(numbers: int) -> Union[str]:
    """Функция маскировки номера банковского счета, Номер счета замаскирован
    и отображается в формате **XXXX, где X — это цифра номера"""

    str_num = str(numbers)
    return f"**{str_num[-4:]}"


# print(get_mask_card_number(7000792289606361))
# print(get_mask_account(73654108430135874305))
