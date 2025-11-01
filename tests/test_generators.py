import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


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
def test_filter_by_currency(transactions, expected):
    """Функция, проверяющая, что функция корректно фильтрует транзакции по заданной валюте."""
    usd_transactions = filter_by_currency(transactions, "USD")
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
def test_filter_by_currency_rub(transactions, expected):
    """Функция, проверяющая, что функция корректно фильтрует транзакции по заданной валюте."""
    usd_transactions = filter_by_currency(transactions, "RUB")
    for _ in range(1):
        assert next(usd_transactions) == expected


def test_filter_by_currency_absent_carrrency(transactions):
    """Функция, проверяющая, что функция правильно обрабатывает случаи, когда транзакции в заданной
    валюте отсутствуют."""
    usd_transactions = filter_by_currency(transactions, "DZD")
    assert list(usd_transactions) == []


def test_filter_by_currency_no_carrrency(transactions_no_currency):
    """Функция, проверяющая случаи поиска без соответствующих валютных операций."""
    assert list(filter_by_currency([])) == []
    assert list(filter_by_currency({})) == []
    assert list(filter_by_currency(None)) == []
    for _ in range(4):
        assert list(filter_by_currency([transactions_no_currency[_]])) == []


# генератор transaction_descriptions
@pytest.mark.parametrize(
    "expected",
    [
        [
            "Перевод организации",
            "Перевод со счета на счет",
            "Перевод со счета на счет",
            "Перевод с карты на карту",
            "Перевод организации",
        ]
    ],
)
def test_transaction_descriptions(transactions, expected):
    """Функция, проверяющая, что функция корректно фильтрует транзакции по заданной валюте."""
    descriptions = transaction_descriptions(transactions)
    for _ in range(5):
        assert next(descriptions) == expected[_]


def test_transaction_descriptions_no_description(transactions_no_currency):
    """Функция, проверяющая случаи поиска без соответствующих валютных операций."""
    assert list(transaction_descriptions([])) == []
    assert list(transaction_descriptions({})) == []
    assert list(transaction_descriptions(None)) == []
    for _ in range(4):
        assert list(transaction_descriptions([transactions_no_currency[_]])) == []


# Тестирование генератора  card_number_generator
@pytest.mark.parametrize(
    "expected",
    [
        [
            "0000 0000 0000 0001",
            "0000 0000 0000 0002",
            "0000 0000 0000 0003",
            "0000 0000 0000 0004",
            "0000 0000 0000 0005",
        ],
    ],
)
def test_card_number_generator(expected):
    """Функция, проверяющая, что функция корректно фильтрует транзакции по заданной валюте."""
    for _ in range(5):
        assert list(card_number_generator(1, 5))[_] == expected[_]
    assert list(card_number_generator(9999_9999_9998_9999, 9999_9999_9998_9999))[0] == "9999 9999 9998 9999"
    assert list(card_number_generator(9999_9999_9999_9999, 9999_9999_9999_9999))[0] == "9999 9999 9999 9999"
    assert list(card_number_generator(5_9999_9999, 6_0000_0000))[0] == "0000 0005 9999 9999"
    assert list(card_number_generator(5_9999_9999, 6_0000_0001))[1] == "0000 0006 0000 0000"
    assert list(card_number_generator(1, 1))[0] == "0000 0000 0000 0001"


def test_card_number_generator_no_correct():
    """Функция, проверяющая случаи поиска без соответствующих валютных операций."""
    mum_stop = 9999_9999_9999_9999
    mum_stop += 2
    # with pytest.raises(TypeError):
    #     list(card_number_generator(44.5, 22))
    # with pytest.raises(TypeError):
    #     list(card_number_generator("a", "d"))
    # with pytest.raises(TypeError):
    #     list(card_number_generator([], 7))
    assert list(card_number_generator(2, None)) == []
    assert list(card_number_generator(9999_9999_9999_9998, mum_stop)) == []
    assert list(card_number_generator(None, None)) == []
    assert list(card_number_generator(-1, 2)) == []
    assert list(card_number_generator(0, 1)) == []
    assert list(card_number_generator(5, 2)) == []
    assert list(card_number_generator(5, -2)) == []
