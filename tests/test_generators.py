import pytest

from src.generators import filter_by_currency, transaction_descriptions


@pytest.mark.parametrize(
    "expected",
    [
        [
            {
                "id": 939719570,
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572",
                "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                "description": "Перевод организации",
                "from": "Счет 75106830613657916952",
                "to": "Счет 11776614605963066702",
            },
            {
                "date": "2019-04-04T23:20:05.206878",
                "description": "Перевод со счета на счет",
                "from": "Счет 19708645243227258542",
                "id": 142264268,
                "operationAmount": {"amount": "79114.93", "currency": {"code": "USD", "name": "USD"}},
                "state": "EXECUTED",
                "to": "Счет 75651667383060284188",
            },
        ]
    ],
)
def test_filter_by_currency(test_lists_transaction, expected):
    """Функция, проверяющая, что функция корректно фильтрует транзакции по заданной валюте."""
    usd_transactions = filter_by_currency(test_lists_transaction, "USD")
    for _ in range(2):
        assert next(usd_transactions) == expected[_]


@pytest.mark.parametrize(
    "expected",
    [
        {
            "date": "2019-03-23T01:09:46.296404",
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "id": 873106923,
            "operationAmount": {"amount": "43318.34", "currency": {"code": "RUB", "name": "руб."}},
            "state": "EXECUTED",
            "to": "Счет 74489636417521191160",
        }
    ],
)
def test_filter_by_currency_rub(test_lists_transaction, expected):
    """Функция, проверяющая, что функция корректно фильтрует транзакции по заданной валюте."""
    usd_transactions = filter_by_currency(test_lists_transaction, "RUB")
    for _ in range(1):
        assert next(usd_transactions) == expected


def test_filter_by_currency_absent_carrrency(test_lists_transaction):
    """Функция, проверяющая, что функция правильно обрабатывает случаи, когда транзакции в заданной валюте отсутствуют."""
    usd_transactions = filter_by_currency(test_lists_transaction, "DZD")
    assert list(usd_transactions) == []


def test_filter_by_currency_no_carrrency(test_lists_transaction_no_currency):
    """Функция, проверяющая случаи поиска без соответствующих валютных операций."""
    assert list(filter_by_currency([])) == []
    assert list(filter_by_currency(None)) == []
    for i in range(4):
        assert list(filter_by_currency([test_lists_transaction_no_currency[i]])) == []
    if i > 4:
        assert list(filter_by_currency(test_lists_transaction_no_currency[i])) == []




# генератор transaction_descriptions

@pytest.mark.parametrize(
    "expected",
    [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации",
    ],
)
def test_transaction_descriptions(test_lists_transaction, expected):
    """Функция, проверяющая, что функция корректно фильтрует транзакции по заданной валюте."""
    usd_transactions = transaction_descriptions(test_lists_transaction)
    for _ in range(5):
        assert next(usd_transactions) == expected
