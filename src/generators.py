from typing import Any


def filter_by_currency(transactions: list[dict], currency: str = 'USD')   ->  Any | None :
    """
    Функция возвращает итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной
    :param transactions: список словарей, представляющих транзакции.
    :param currency:валюта операции
    :return: итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной
    """
    if  transactions is None or len(transactions) == 0 :
        return 'Список транзакций пуст'

    for current_dict in transactions:
        operation_amount = current_dict.get("operationAmount")
        if operation_amount is not None:
            currency_info = operation_amount.get("currency")
            if currency_info is not None:
                code = currency_info.get("code")
                if code is None:
                    return "Информация о сумме операции не найдена"
            else:
                return "Информация о валюте не найдена"
        else:
            return "Информация о сумме операции не найдена"

        for transaction in transactions:
             if transaction["operationAmount"]["currency"]["code"] == currency:
                yield  transaction
    return  "Информация не найдена"


def transaction_descriptions(transactions: list[dict])   ->  Any | None :
    """
    Функция, который принимает список словарей с транзакциями и возвращает описание каждой операции по очереди.
    :param transactions: список словарей, представляющих транзакции.
    :return: возвращает описание каждой операции по очереди.
    """
    if  transactions is None or len(transactions) == 0 :
        return 'Список транзакций пуст'

    for current_dict in transactions:
        operation_amount = current_dict.get("description")
        if operation_amount is  None:
            return "Информация о переводе отсутствует"
        else:
            yield current_dict.get("description")

