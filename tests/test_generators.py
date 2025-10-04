import pytest

from src.generators import filter_by_currency


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
                "id": 142264268,
                "state": "EXECUTED",
                "date": "2019-04-04T23:20:05.206878",
                "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
                "description": "Перевод со счета счет",
                "from": "Счет 19708645243227258542",
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
    [[]],
)
def test_filter_by_currency_absent_carrrency(test_lists_transaction, expected):
    """Функция, проверяющая, что функция правильно обрабатывает случаи, когда транзакции в заданной валюте отсутствуют."""
    usd_transactions = filter_by_currency(test_lists_transaction, "DZD")
    assert list(usd_transactions) == expected


def test_filter_by_currency_no_list():
    """Функция, проверяющая, что генератор не завершается ошибкой при обработке пустого списка или списка без
    соответствующих валютных операций."""
    # usd_transactions = filter_by_currency(test_lists_transaction_no_corrency, "USD")
    assert list(filter_by_currency([])) == []


def test_filter_by_currency_no_carrrency(test_lists_transaction_no_corrency):
    """Функция, проверяющая, что функция правильно обрабатывает случаи, когда транзакции в заданной валюте
    отсутствуют."""
    assert list(filter_by_currency(test_lists_transaction_no_corrency)) == []

@pytest.mark.parametrize(
    "list_no_correct,expected",
    [
        ({
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },[]),
        ({
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currenc":{"name": "USD", "code1": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },[]),
    ],
)
def test_filter_by_currency_no_carrrency2(list_no_correct,expected):
    """Функция, проверяющая, что функция правильно обрабатывает случаи, когда транзакции в заданной валюте
    отсутствуют."""
    assert list(filter_by_currency(list_no_correct)) == expected




# Убедитесь, что генератор не завершается ошибкой при обработке пустого списка или списка без соответствующих валютных операций.
