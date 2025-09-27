import pytest

from src.masks import get_mask_card_number, get_mask_account
from src.widget import mask_account_card, get_date


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
@pytest.mark.parametrize("numbers", [70070922896063261, 770070922896063261, 70003432606362, 0])
def test_get_mask_card_number_correct_len(numbers):
    with pytest.raises(ValueError):
        get_mask_card_number(numbers)


@pytest.mark.parametrize("numbers", [77007092289606.3, "0000000000000000", "7700709228960632"])
def test_get_mask_card_number_correct_type(numbers):
    with pytest.raises(TypeError):
        get_mask_card_number(numbers)


# Проверка, что функция корректно обрабатывает входные строки, где отсутствует номер карты.
@pytest.mark.parametrize("numbers", [None, (), ""])
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
    "numbers", [7700709228963333333.3, "000000000000000000000", 0.0, "770070922896333333300", None, ""]
)
def test_get_mask_account_correct_type(numbers):
    with pytest.raises(TypeError):
        get_mask_account(numbers)


# Проверка работы функции с различными длинами номеров счетов.
# Проверка, что функция корректно обрабатывает входные данные, где номер счета меньше ожидаемой длины.
@pytest.mark.parametrize("numbers", [700709228962896063261, 77007092282313196063261, 7700323370922893, 342, 0])
def test_get_mask_account_correct_len(numbers):
    with pytest.raises(ValueError):
        get_mask_account(numbers)


# Модуль widget
# Функция  mask_account_card:
# Тесты для проверки, что функция корректно распознает и применяет нужный тип маскировки в зависимости от типа входных
# данных (карта или счет).
# Параметризованные тесты с разными типами карт и счетов для проверки универсальности функции.
@pytest.mark.parametrize(
    "init_str,  expected",
    [
        ("Maestro 1596837868705199", "Maestro 11596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 77158 30** **** 6758"),
        ("Visa Classic 6831982476737658", "Visa Classic 66831 98** **** 7658"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_mask_account_card(init_str, expected):
    assert mask_account_card(init_str) == expected


# Тестирование функции на обработку некорректных входных данных и проверка ее устойчивости к ошибкам.
@pytest.mark.parametrize(
    "init_str",
    [
        ("Maestro1596837868705199"),
        ("Maestro 0"),
        ("Maestro 1596837833368705199"),
        ("64686473678894779589"),
        ("Visa Classic 6ввв831982476737658"),
        ("Visa Classic "),
        ("СЧЕТ73654108430135874405"),
        ("Счет ****************"),
        ("Visa Classic 6831982476737658 *****"),
        ("СЧЕТ"),
        ("Счет "),
        ("Счет 64686473678894-79589"),
        ("Счет 44473654108430135874304"),
        ("Счет73654108430135874302"),
        ("Счет 00"),
        ("Счет 64686473678894779.89"),
    ],
)
def test_mask_account_card_correct_value(init_str):
    with pytest.raises(ValueError):
        mask_account_card(init_str)


@pytest.mark.parametrize(
    "init_str",
    [
        None,
        "None",
        64686473678894779.89,
        7700709228960632,
        (),
        0,
        .0,
        "Maestro 1596837868705.99",
        "Maestro 99 1596837868705999",
    ],
)
def test_mask_account_card_correct_type(init_str):
    with pytest.raises(TypeError):
        mask_account_card(init_str)


@pytest.mark.parametrize(
    "init_str",
    [
        64686473678894779.89,
        (),
        7700709228960632,
        0000000000000000,
    ],
)
def test_mask_account_card_correct_type(init_str):
    with pytest.raises(AttributeError):
        mask_account_card(init_str)


# Функция get_date:
# Тестирование правильности преобразования даты.
@pytest.mark.parametrize(
    "date_str,  expected",
    [("2024-03-11T02:26:18.671407", "11.03.2024"), ("2020-01-10T02:26:18.671407", "10.01.2020")],
)
def test_get_date(date_str, expected):
    assert get_date(date_str) == expected


# Проверка работы функции на различных входных форматах даты, включая граничные случаи и нестандартные строки с датами.
# Проверка, что функция корректно обрабатывает входные строки, где отсутствует дата.
@pytest.mark.parametrize(
    "date_str",
    [
        "671407",
        "2024-03-11 02:26:18.671407",
        "2024-03-11",
        "24-03-11T02:26:18.671407",
        "11.03.2024",
        "11.03.24",
        "",
        "dd-",
        "Wed, 12 April 2023",
    ],
)
def test_get_date_correct_value(date_str):
    with pytest.raises(ValueError):
        get_date(date_str)


# Проверка, что функция корректно обрабатывает входные строки, где отсутствует дата.
@pytest.mark.parametrize(
    "date_str",
    [None, ()],
)
def test_get_date_correct_type(date_str):
    with pytest.raises(TypeError):
        get_date(date_str)
