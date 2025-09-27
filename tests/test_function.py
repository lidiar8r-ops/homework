import pytest

from src.masks import get_mask_card_number, get_mask_account


# """Функция get_mask_card_number:
# Тестирование правильности маскирования номера карты.
@pytest.mark.parametrize(
    "numbers,  expected",
    [(7007092289606361, "7007 09** **** 6361"), (7000343260636210, "7000 34** **** 6210")],
)
def test_get_mask_card_number(numbers, expected):
    assert get_mask_card_number(numbers) == expected


# Проверка работы функции на различных входных форматах номеров карт, включая граничные случаи и нестандартные
# длины номеров.
@pytest.mark.parametrize("numbers", [(70070922896063261), (770070922896063261), (70003432606362)])
def test_get_mask_card_number_correct_len(numbers):
    with pytest.raises(ValueError):
        get_mask_card_number(numbers)


@pytest.mark.parametrize("numbers", [(77007092289606.3), (0000000000000000), ("7700709228960632")])
def test_get_mask_card_number_correct_type(numbers):
    with pytest.raises(TypeError):
        get_mask_card_number(numbers)


# Проверка, что функция корректно обрабатывает входные строки, где отсутствует номер карты.
@pytest.mark.parametrize("numbers", [(), (0)])
def test_get_mask_card_number_correct_empty(numbers):
    with pytest.raises(TypeError):
        get_mask_card_number(numbers)


# """Функция get_mask_account:
# Тестирование правильности маскирования номера счета.
@pytest.mark.parametrize(
    "numbers,  expected",
    [(73654108430135874305, "**4305"), (73654108430135874000, "**4000")],
)
def test_get_mask_account(numbers, expected):
    assert get_mask_account(numbers) == expected


# Проверка работы функции с различными форматами
@pytest.mark.parametrize(
    "numbers", [(7700709228963333333.3), (000000000000000000000), ("770070922896333333300"), (), (0)]
)
def test_get_mask_account_correct_type(numbers):
    with pytest.raises(TypeError):
        get_mask_account(numbers)


# Проверка работы функции с различными длинами номеров счетов.
# Проверка, что функция корректно обрабатывает входные данные, где номер счета меньше ожидаемой длины.
@pytest.mark.parametrize(
    "numbers", [700709228962896063261, 77007092282313196063261, 7700709228963333333, 7700323370922893, 342]
)
def test_get_mask_account_correct_len(numbers):
    with pytest.raises(ValueError):
        get_mask_account(numbers)



