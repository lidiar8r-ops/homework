from unittest.mock import patch, Mock
import requests
from src.external_api import get_currency_exchange


@patch('requests.get')
def test_euro_to_rub_conversion(self, mock_get):
    """Проверка правильной конвертации EUR->RUB"""
    # Настройка моков (фиктивных запросов)
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {'result': 80.0}
    mock_get.return_value = mock_response

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
    self.assertAlmostEqual(actual_result, expected_result)

def test_ruble_amount(self):
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
    self.assertEqual(actual_result, expected_result)

def test_zero_amount(self):
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
    self.assertEqual(actual_result, expected_result)

@patch('requests.get')
def test_http_error(self, mock_get):
    """Проверка реакции на сетевую ошибку (код статуса отличающийся от 200)"""
    mock_response = Mock()
    mock_response.status_code = 404
    mock_get.return_value = mock_response

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
    self.assertEqual(actual_result, expected_result)


@patch('requests.get')  # Патчим реальный объект `requests.get`
def test_json_decode_error(self, mock_get):
    """Проверка реакции на некорректный JSON от API."""
    # Создаем поддельный объект ответа
    mock_response = Mock()
    mock_response.status_code = 200  # Статус успешный, но тело JSON неправильное
    mock_response.json.side_effect = json.decoder.JSONDecodeError('', '', 0)  # Исключение при попытке парсинга JSON
    mock_get.return_value = mock_response  # Возвращаем подделанный ответ

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
    with raises(json.decoder.JSONDecodeError):
        get_currency_exchange(transaction)