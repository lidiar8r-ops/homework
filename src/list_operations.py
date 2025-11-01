import logging
import os
import re
from collections import Counter
from typing import Dict, List

# Получаем директорию текущего файла (т.е. папку src)
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
# Формируем абсолютный путь к папке log (которая находится на уровень выше)
LOG_DIR = os.path.join(CURRENT_DIR, "..", "logs")
log_file_path = os.path.join(LOG_DIR, "list_operation.log")

logger_list_operation = logging.getLogger("list_operation")
file_handler_list_operation = logging.FileHandler(log_file_path, "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler_list_operation.setFormatter(file_formatter)
logger_list_operation.addHandler(file_handler_list_operation)
logger_list_operation.setLevel(logging.DEBUG)


def process_bank_search(data: List[Dict], search_str: str) -> List[Dict]:
    """
    Ищет в списке банковских операций записи, где в поле 'description'
    содержится заданная строка (с учётом частичного совпадения и без учёта регистра).
    :param data:список словарей с данными о банковских операциях
    :param search: строка поиска  в поле description
    :return:список словарей, где в description найдено совпадение с search
    """
    # Создаем шаблон регулярного выражения
    # re.escape - экранирует специальные символы в строке поиска
    # flags=re.IGNORECASE - поиск без учёта регистра
    pattern = re.compile(search_str, flags=re.IGNORECASE)
    result = []
    for transaction in data:
        # Пропускаем транзакции с некорректной структурой
        if "description" not in transaction:
            logger_list_operation.error(f'Пропущена транзакция - нет поля "description": {transaction}')
            continue
        if pattern.search(transaction.get("description", "")):
            result.append(transaction)

    return result


def process_bank_operations(data: List[Dict], categories: List[str]) -> Dict[str, int]:
    """
    Принимает список словарей с данными о банковских операциях и список категорий.
    Возвращает словарь, где ключи — названия категорий, значения — количество операций,
    в которых description содержит соответствующую категорию (подстроку).

    :param data: список словарей с данными о банковских операциях (поле description обязательно)
    :param categories: список строк‑подстрок для поиска в поле description
    :return: словарь {категория: количество операций}
    """
    # Список для накопления найденных категорий
    matched_categories = []

    # Проходим по каждой операции в данных
    for operation in data:
        try:
            description = operation.get("description", "").upper()  # Приводим к нижнему регистру

            # Проверяем каждую категорию
            for category in categories:
                if category.upper() in description:
                    matched_categories.append(category)
        except Exception as e:
            # пропускаем
            logger_list_operation.error(f"Ошибка при обработке данных: {e}.Данные: {operation}")
            matched_categories.append("")

    # Создаём Counter из найденных категорий
    counter = Counter(matched_categories)

    # Инициализируем результат со всеми категориями (включая те, что не встретились)
    result = {category: counter.get(category, 0) for category in categories}

    return result
