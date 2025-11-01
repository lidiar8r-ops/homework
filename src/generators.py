import logging
import os
from typing import Any, Dict, Iterator, List

# Получаем директорию текущего файла (т.е. папку src)
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
# Формируем абсолютный путь к папке log (которая находится на уровень выше)
LOG_DIR = os.path.join(CURRENT_DIR, "..", "logs")
log_file_path = os.path.join(LOG_DIR, "geneators.log")

logger_generators = logging.getLogger("geneators")
file_handler_geneators = logging.FileHandler(log_file_path, "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler_geneators.setFormatter(file_formatter)
logger_generators.addHandler(file_handler_geneators)
logger_generators.setLevel(logging.DEBUG)


def filter_by_currency(transactions: List[Dict], currency: str = "USD") -> Iterator[Dict]:
    """
    Функция возвращает итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной.
    :param transactions: список словарей, представляющих транзакции.
    :param currency: валюта операции (по умолчанию "USD").
    :return: итератор, выдающий транзакции с заданной валютой.
    """
    if transactions is None or transactions == [] or transactions == {}:
        logger_generators.error("Список транзакций пуст")
        return []

    for transaction in transactions:
        try:
            transaction_currency = transaction.get("operationAmount", "").get("currency", "").get("code")
            if transaction_currency == currency:
                yield transaction
        except Exception as e:
            # Пропускаем транзакции с некорректной структурой
            logger_generators.error(
                f"Неожиданная ошибка при обработке транзакции: {type(e).__name__}: {e}. "
                f"Данные транзакции: {transaction}"
            )

            # print(f" Пропущена транзакция из-за отсутствующего ключа: {e}")
            continue


def transaction_descriptions(transactions: List[Dict]) -> Any:
    """
    Функция, который принимает список словарей с транзакциями и возвращает описание каждой операции по очереди.
    :param transactions: список словарей, представляющих транзакции.
    :return: возвращает описание каждой операции по очереди.
    """
    if transactions is None or transactions == [] or transactions == {} or len(transactions) == 0:
        logger_generators.error("Список транзакций пуст")
        return []

    for current_dict in transactions:
        operation_amount = current_dict.get("description")
        if operation_amount is None:
            logger_generators.error(f"Отсутствуюет ключ description в транзакции {current_dict}")
        else:
            yield operation_amount


def card_number_generator(start: int, stop: int) -> Any:
    """
    генератор, который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX, где X — цифра номера карты.
    Генератор может сгенерировать номера карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999.
    :param start: начальное значения для генерации диапазона номеров.
    :param stop:  конечное значения для генерации диапазона номеров.
    :return: номера банковских карт в форматеXXXX XXXX XXXX XXXX, где X — цифра номера карты.
    """
    if start is None:
        logger_generators.error("Не задано начальное значения для генерации диапазона номеров")
        return "Не задано начальное значения для генерации диапазона номеров"
    if stop is None:
        logger_generators.error("Не задано начальное значения для генерации диапазона номеров")
        return "Не задано начальное значения для генерации диапазона номеров"
    if start <= 0:
        logger_generators.error("Не верно задано конечное значения для генерации диапазона номеров")
        return "Не верно задано конечное значения для генерации диапазона номеров"
    if stop <= 0:
        logger_generators.error("Не верно задано конечное значения для генерации диапазона номеров")
        return "Не верно задано конечное значения для генерации диапазона номеров"
    if not str(start).isdigit() or not str(stop).isdigit():
        # raise TypeError("Не соответствие типов")
        logger_generators.error("Не соответствие типов")
        return ""

    if stop > 9999_9999_9999_9999:
        logger_generators.error("Не верно задано конечное значения для генерации диапазона номеров")
        return "Не верно задано конечное значения для генерации диапазона номеров"

    if start > stop:
        logger_generators.error("Конечное значение не может быть меньше чем начальное значение")
        return "Конечное значение не может быть меньше чем начальное значение"

    for number in range(start, stop + 1):
        if number <= stop:
            str_number = str(number).zfill(16)
            str_num = f"{str_number[0:4]} {str_number[4:8]} {str_number[8:12]} {str_number[-4:]}"
            yield str_num
