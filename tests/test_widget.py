import pytest

from src.widget import get_date, mask_account_card


# Модуль widget
# Функция  mask_account_card:
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
    """для проверки, что функция корректно распознает и применяет нужный тип маскировки в зависимости от типа входных
    данных (карта или счет)."""
    assert mask_account_card(init_str) == expected


# @pytest.mark.parametrize(
#     "init_str",
#     [
#         "Maestro1596837868705199",
#         "Maestro 1596837833368705199",
#         "64686473678894779589",
#         "Visa Classic 6ввв831982476737658",
#         "Visa Classic ",
#         "СЧЕТ73654108430135874405",
#         "Счет ****************",
#         "Visa Classic 6831982476737658 *****",
#         "Счет ",
#         "Счет 64686473678894-79589",
#         "Счет 44473654108430135874304",
#         "Счет73654108430135874302",
#         "Счет 64686473678894779.89",
#     ],
# )
# def test_mask_account_card_correct_value(init_str):
#     """для проверки, корректно заполненных данных"""
#     with pytest.raises(ValueError):
#         mask_account_card(init_str)


# @pytest.mark.parametrize(
#     "init_str",
#     [
#         None,
#         "Maestro 0",
#         "Счет 00",
#     ],
# )
# def test_mask_account_card_correct_type(init_str):
#     """для проверки, корректно заполненных типов данных"""
#     with pytest.raises(TypeError):
#         mask_account_card(init_str)


# @pytest.mark.parametrize(
#     "init_str",
#     [
#         True,
#     ],
# )
# def test_mask_account_card_correct_attribute(init_str):
#     """для проверки, корректно заполненных типов данных"""
#     with pytest.raises(AttributeError):
#         mask_account_card(init_str)
#
#
# # Функция get_date:
@pytest.mark.parametrize(
    "date_str,  expected",
    [("2024-03-11T02:26:18.671407", "11.03.2024"), ("2020-01-10T02:26:18.671407", "10.01.2020")],
)
def test_get_date(date_str, expected):
    """Тестирование правильности преобразования даты."""
    assert get_date(date_str) == expected

#
# @pytest.mark.parametrize(
#     "date_str",
#     [
#         "671407",
#         "2024-03-11 02:26:18.671407",
#         "2024-03-11",
#         "24-03-11T02:26:18.671407",
#         "11.03.2024",
#         "11.03.24",
#         "",
#         "dd-",
#         "Wed, 12 April 2023",
#     ],
# )
# def test_get_date_correct_value(date_str):
#     """Проверка работы функции на различных входных форматах даты, включая граничные случаи и нестандартные
#     строки с датами. Проверка, что функция корректно обрабатывает входные строки, где отсутствует дата."""
#     with pytest.raises(ValueError):
#         get_date(date_str)
#
#
# @pytest.mark.parametrize(
#     "date_str",
#     [None, (), True, False],
# )
# def test_get_date_correct_type(date_str):
#     """Проверка работы функции на различных входных форматах даты
#     Проверка, что функция корректно обрабатывает входные строки, где отсутствует дата."""
#     with pytest.raises(TypeError):
#         get_date(date_str)
