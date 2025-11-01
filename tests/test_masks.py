import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "numbers,  expected",
    [(7007092289606361, "7007 09** **** 6361"), (7000343260636210, "7000 34** **** 6210")],
)
def test_get_mask_card_number(numbers, expected):
    """Функция get_mask_card_number:
    Тестирование правильности маскирования номера карты."""
    assert get_mask_card_number(numbers) == expected


# @pytest.mark.parametrize("numbers", [70070922896063261, 770070922896063261, 70003432606362])
# def test_get_mask_card_number_correct_len(numbers):
#     """Проверка работы функции на различных входных форматах номеров карт, включая граничные случаи и нестандартные
#     длины номеров."""
#     with pytest.raises(ValueError):
#         get_mask_card_number(numbers)
#
#
# @pytest.mark.parametrize("numbers", [77007092289606.3, "0000000000000000", "7700709228960632", 0])
# def test_get_mask_card_number_correct_type(numbers):
#     """Проверка работы функции на различных входных форматах номеров карт, несоответствующих типов"""
#     with pytest.raises(TypeError):
#         get_mask_card_number(numbers)
#
#
# @pytest.mark.parametrize("numbers", [None, (), ""])
# def test_get_mask_card_number_correct_empty(numbers):
#     """Проверка, что функция корректно обрабатывает входные строки, где отсутствует номер карты."""
#     with pytest.raises(TypeError):
#         get_mask_card_number(numbers)
#

@pytest.mark.parametrize(
    "numbers,  expected",
    [(73654108430135874305, "**4305"), (73654108430135874000, "**4000")],
)
def test_get_mask_account(numbers, expected):
    """Функция get_mask_account:
    Тестирование правильности маскирования номера счета."""
    assert get_mask_account(numbers) == expected

#
# @pytest.mark.parametrize(
#     "numbers",
#     [
#         7700709228963333333.3,
#         "000000000000000000000",
#         0.0,
#         "770070922896333333300",
#         None,
#         "",
#         "a",
#         "0",
#         0,
#     ],
# )
# def test_get_mask_account_correct_type(numbers):
#     """Проверка работы функции с различными форматами"""
#     with pytest.raises(TypeError):
#         get_mask_account(numbers)
#

# @pytest.mark.parametrize("numbers", [700709228962896063261, 77007092282313196063261, 7700323370922893, 342])
# def test_get_mask_account_correct_len(numbers):
#     """Проверка работы функции с различными длинами номеров счетов.
#     Проверка, что функция корректно обрабатывает входные данные, где номер счета меньше ожидаемой длины.
#     """
#     with pytest.raises(ValueError):
#         get_mask_account(numbers)
