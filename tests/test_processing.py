import pytest

from src.processing import filter_by_state, sort_by_date


# Модуль processing
# Функция filter_by_state:
@pytest.mark.parametrize(
    "state, expected",
    [
        (
            "CANCELED",
            [
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
        ),
        (
            "EXECUTED",
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
    ],
)
def test_filter_by_state(test_lists, state, expected):
    """Тестирование фильтрации списка словарей по заданному статусу state.
    Параметризация тестов для различных возможных значений статуса state."""
    assert filter_by_state(test_lists, state) == expected
    assert filter_by_state(test_lists, state) == expected


# def test_filter_by_state_correct_key(test_lists_no_correct_key):
#     """Проверка работы функции при отсутствии словарей с ключом state в списке."""
#     with pytest.raises(KeyError):
#         filter_by_state(test_lists_no_correct_key)


@pytest.mark.parametrize(
    "state, expected",
    [
        ("CANCELED ", []),
        ("EXECUTE", []),
    ],
)
def test_filter_by_state_correct_value(test_lists, state, expected):
    """Проверка работы функции при отсутствии словарей с указанным статусом state в списке."""
    assert filter_by_state(test_lists, state) == expected


# Функция sort_by_date:
@pytest.mark.parametrize(
    "sorting, expected",
    [
        (
            True,
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            False,
            [
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            ],
        ),
    ],
)
def test_sort_by_date(test_lists, sorting, expected):
    """Тестирование сортировки списка словарей по датам в порядке убывания и возрастания."""
    assert sort_by_date(test_lists, sorting) == expected
    assert sort_by_date(test_lists, sorting) == expected


@pytest.mark.parametrize(
    "sorting, expected",
    [
        (
            True,
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 594226726, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            False,
            [
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226726, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            ],
        ),
    ],
)
def test_sort_by_date_similar(test_lists_date_similar, sorting, expected):
    """Проверка корректности сортировки при одинаковых датах."""
    assert sort_by_date(test_lists_date_similar, sorting) == expected

#
# def test_sort_by_date_correct_value(test_lists_no_correct_date):
#     """Тесты на работу функции с некорректными или нестандартными форматами дат."""
#     with pytest.raises(ValueError):
#         sort_by_date(test_lists_no_correct_date)
#
#
# def test_sort_by_date_correct_type(test_lists_no_correct_no_date):
#     """Тест на работу функции с некорректными или нестандартными форматами дат."""
#     with pytest.raises(TypeError):
#         sort_by_date(test_lists_no_correct_no_date)
#
#
# def test_sort_by_date_correct_key(test_lists_no_correct_key):
#     """Проверка работы функции при отсутствии словарей с ключом state в списке."""
#     with pytest.raises(KeyError):
#         sort_by_date(test_lists_no_correct_key)
