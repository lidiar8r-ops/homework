from unittest.mock import patch, Mock
import pytest
from src.external_api import get_currency_exchange



@pytest.fixture
def mock_request():
    with patch('requests.get') as mocked_get:
        yield mocked_get


def test_euro_to_rub_conversion(mock_request):
    """Проверка правильной конвертации EUR->RUB"""
    # Настройка моков (фиктивных запросов)
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {'result': 80.0}
    mock_request.return_value = mock_response

    # Пример транзакции в евро
    transaction = {
        "operationAmount": {
            "amount": 1,
            "currency": {
                "code": "EUR"
            }
        }
    }

    expected_result = 80.0
    actual_result = get_currency_exchange(transaction)
    assert abs(expected_result - actual_result) < 0.001  # сравнение чисел с плавающей точкой


def test_ruble_amount():
    """Проверка правильности обработки рублей (без обращения к API)"""
    transaction = {
        "operationAmount": {
            "amount": 100,
            "currency": {
                "code": "RUB"
            }
        }
    }

    expected_result = 100.0
    actual_result = get_currency_exchange(transaction)
    assert expected_result == actual_result


def test_zero_amount():
    """Проверка реакции на операцию с нулевым значением"""
    transaction = {
        "operationAmount": {
            "amount": 0,
            "currency": {
                "code": "USD"
            }
        }
    }

    expected_result = 0
    actual_result = get_currency_exchange(transaction)
    assert expected_result == actual_result


def test_http_error(mock_request):
    """Проверка реакции на сетевую ошибку (код статуса отличающийся от 200)"""
    mock_response = Mock()
    mock_response.status_code = 404
    mock_request.return_value = mock_response

    transaction = {
        "operationAmount": {
            "amount": 10,
            "currency": {
                "code": "EUR"
            }
        }
    }

    expected_result = 0
    actual_result = get_currency_exchange(transaction)
    assert expected_result == actual_result

@pytest.fixture
def mock_request():
    with patch('requests.get') as mocked_get:
        yield mocked_get

def test_json_decode_error(mock_request):
    """Проверка реакции на некорректный JSON от API."""
    # Создание мока ответа
    mock_response = Mock()
    mock_response.status_code = 200  # статус успешный, но JSON неправильный
    mock_response.json.side_effect = json.decoder.JSONDecodeError('', '', 0)  # Исключение при чтении JSON
    mock_request.return_value = mock_response  # возвращаем подставленный ответ

    # Транзакция в валюте EUR
    transaction = {
        "operationAmount": {
            "amount": 10,
            "currency": {
                "code": "EUR"
            }
        }
    }

    # Ожидается исключение JSONDecodeError
    with pytest.raises(json.decoder.JSONDecodeError):
        get_currency_exchange(transaction)