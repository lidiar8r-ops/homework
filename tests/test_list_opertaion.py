import logging

import pytest

from src.list_operations import process_bank_operations, process_bank_search


# Тестирование функции поиска банковской операции по описанию
@pytest.mark.parametrize(
    "search_string, expected_result",
    [
        (
            "перевод",
            [
                {
                    "id": 142264268,
                    "state": "EXECUTED",
                    "date": "2019-04-04T23:20:05.206878",
                    "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод со счета на счет",
                    "from": "Счет 19708645243227258542",
                    "to": "Счет 75651667383060284188",
                },
                {
                    "id": 615064591,
                    "state": "CANCELED",
                    "date": "2018-10-14T08:21:33.419441",
                    "operationAmount": {"amount": "77751.04", "currency": {"name": "руб.", "code": "RUB"}},
                    "description": "Перевод с карты на счет",
                    "from": "Maestro 3928549031574026",
                    "to": "Счет 84163357546688983493",
                },
            ],
        ),
        ("счетов", []),
        # ("описания", ""),
        ("несуществующая операция", []),
    ],
)
def test_process_bank_search(test_bank_transactions, search_string, expected_result):
    """Проверяет поиск банковской операции по полю description."""
    data = test_bank_transactions  # получаем данные один раз
    result = process_bank_search(data, search_string)

    # Сравниваем списки словарей по содержимому (не по ссылкам)
    assert len(result) == len(expected_result)
    for expected_item in expected_result:
        assert any(all(result_item[k] == expected_item[k] for k in expected_item) for result_item in result)


# Тестирование группировки операций по категориям
@pytest.mark.parametrize(
    "categories, expected_result",
    [
        (
            ["Перевод со счета на счет", "Открытие вклада", "Перевод с карты на счет", ""],
            {"": 6, "Открытие вклада": 1, "Перевод с карты на счет": 1, "Перевод со счета на счет": 1},
        ),
        ([], {}),
        (set(), {}),
    ],
)
def test_process_bank_operations(test_bank_transactions, categories, expected_result):
    """
    Проверяет группировку операций по категориям.
    """
    result = process_bank_operations(test_bank_transactions, categories)
    # фильтруем результат, оставляя только нужные категории
    filtered_result = {k: v for k, v in result.items() if any(cat.upper() in k.upper() for cat in categories)}
    assert filtered_result == expected_result


def test_process_bank_operations_exception_logging(caplog):
    """
    При ошибке в обработке данных — логируется исключение, возвращается пустой словарь.
    """
    broken_data = [{"description": ["нехешируемый", "список"]}, {"description": "нормальная операция"}]
    result = process_bank_operations(broken_data, categories=["тест"])
    print(result)
    with caplog.at_level(logging.ERROR, logger="list_operation"):
        result = process_bank_operations(broken_data, categories=["тест"])

    assert result == {'тест': 0}
    error_records = [r for r in caplog.records if r.levelno >= logging.ERROR]
    assert len(error_records) > 0
    assert all(r.name == "list_operation" for r in error_records)

    # Исправленная проверка сообщений
    assert any(
        "ошибка" in r.message.lower() or "error" in r.message.lower() or "type" in r.message.lower()
        for r in error_records
    )
