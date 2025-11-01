import tempfile
from pathlib import Path
from unittest.mock import patch

import pandas as pd

from src.get_csv_xls import get_csv_xlsx_reader_transaction


def test_success_csv(tmp_path, mock_isfile, mock_read_csv, mock_read_excel_ok, mock_df):
    """тест на успешность получения данных из csv. Вызывает функцию и проверяет, что результат — список,
    и данные внутри соответствуют ожидаемым."""
    # Создаем временный CSV файл
    file_path = Path(tempfile.gettempdir()) / "test.csv"
    file_path.write_text(
        "id;state;date;amount;currency_name;currency_code;from;to;description\n"
        "1;done;2023-01-01;100;USD;USD;A;B;Test transaction"
    )

    mock_isfile().return_value = True
    mock_read_csv.return_value = mock_df

    result = get_csv_xlsx_reader_transaction(str(file_path))
    assert isinstance(result, list)
    assert result[0]["id"] == "1"
    assert result[0]["operationAmount"]["amount"] == 100


def test_success_excel(mock_isfile, mock_read_excel_ok, mock_df):
    """Тест на успешность получения данных из Excel."""
    # Настраиваем фиктивные условия
    mock_isfile.return_value = True
    mock_read_excel_ok.return_value = mock_df
    file_path = "file.xlsx"

    # Выполняем тестируемую функцию
    result = get_csv_xlsx_reader_transaction(file_path)

    # Основные проверки
    assert isinstance(result, list), f"Результат не является списком: {type(result)}"
    assert len(result) > 0, "Полученный результат пустой."

    # Проверка первого элемента
    first_item = result[0]
    assert first_item["id"] == "1", f"id не совпадает: {first_item['id']}"
    assert first_item["state"] == "done", f"state не совпадает: {first_item['state']}"


def test_headers_only_with_mock(empty_columns_dataframe):
    """Проверяет, что функция возвращает пустой список, когда данных нет.Но заголовки есть"""

    # Создаем DataFrame с только заголовками (пустой)
    with patch("os.path.isfile") as mock_isfile, patch("pandas.read_csv") as mock_read_csv, patch(
        "pandas.read_excel"
    ) as mock_read_excel:
        mock_isfile.return_value = True

        # В зависимости от расширения, вызовется нужная функция
        # Для CSV
        mock_read_csv.return_value = empty_columns_dataframe
        # Для Excel
        mock_read_excel.return_value = empty_columns_dataframe

        # Вызов для CSV
        result_csv = get_csv_xlsx_reader_transaction("empty_date.csv")
        assert result_csv == []

        # Вызов для Excel
        result_xlsx = get_csv_xlsx_reader_transaction("empty_date.xlsx")
        assert result_xlsx == []


def test_nonexistent_file():
    """Тест  обработка ситуации, когда файл не существует"""
    with patch("os.path.isfile", return_value=False):
        result = get_csv_xlsx_reader_transaction("nonexistent.csv")
        assert result == []


def test_incorrect_extension():
    """Тест обработка файла с неправильным расширением"""
    with patch("os.path.isfile", return_value=True):
        result = get_csv_xlsx_reader_transaction("invalid.txt")
        assert result == []


def test_pandas_exception():
    """Тест обработка исключения при работе с Pandas"""
    with patch("pandas.read_csv", side_effect=Exception("Pandas read exception")), patch(
        "os.path.isfile", return_value=True
    ):
        result = get_csv_xlsx_reader_transaction("Pandas_read_exception.csv")
        assert result == []


def test_empty_file():
    """Тест  обработка пустого файла"""
    with patch("pandas.read_csv", return_value=pd.DataFrame()), patch("os.path.isfile", return_value=True):
        result = get_csv_xlsx_reader_transaction("empty.csv")
        assert result == []


def test_missing_column(valid_dataframe):
    """Тест обработка отсутствующих колонок"""
    incomplete_dataframe = [
        {
            "id": 1,
            "state": "CANCELED",
            "date": "2023-09-15",
            "amount": 100,
            "currency_name": "RUB",
            "currency_code": "RUB",
            "description": "Test transaction",
            "from": "Bank A",
        }
    ]  # колонка "to" удалена!
    with patch("pandas.read_csv", return_value=incomplete_dataframe), patch("os.path.isfile", return_value=True):
        result = get_csv_xlsx_reader_transaction("missing_column.csv")
        assert result == []  # "Функция должна вернуть пустой список при отсутствии обязательных полей."


def test_value_error_with_incorrect_csv(csv_temp_file):
    """Тест на неправильное значение (ValueError) в CSV-файле."""
    assert get_csv_xlsx_reader_transaction(csv_temp_file) == []


@patch("pandas.read_csv")
def test_generic_exception(mock_read_csv):
    """Тест на общее исключение (искусственно вызвано в read_csv)."""
    mock_read_csv.side_effect = Exception("Test exception")
    assert get_csv_xlsx_reader_transaction("fake.csv") == []


@patch("pandas.read_excel")
def test_generic_exception_on_excel(mock_read_excel):
    """Тест на общее исключение (искусственно вызвано в read_excel)."""
    mock_read_excel.side_effect = Exception("Test exception")
    assert get_csv_xlsx_reader_transaction("fake.xlsx") == []


# Тест проверяющий создание DataFrame
def test_valid_dataframe(valid_dataframe):
    assert isinstance(valid_dataframe, pd.DataFrame)
    assert len(valid_dataframe.columns) == 9
    assert valid_dataframe.shape == (1, 9)
