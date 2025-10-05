from typing import Any, Generator


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


def card_number_generator(start: int, stop: int) ->  Any | str:
    """
    генератор, который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX, где X — цифра номера карты.
    Генератор может сгенерировать номера карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999.
    :param start: начальное значения для генерации диапазона номеров.
    :param stop:  конечное значения для генерации диапазона номеров.
    :return: номера банковских карт в форматеXXXX XXXX XXXX XXXX, где X — цифра номера карты.
    """
    # if stop isint:
    if start is None:
        return "Не задано начальное значения для генерации диапазона номеров"
    if start < 0 :
        return "Не верно задано конечное значения для генерации диапазона номеров"
    if stop is None:
        return "Не задано начальное значения для генерации диапазона номеров"
    if stop < 0  or stop > 9999_9999_9999_9999:
        return "Не верно задано конечное значения для генерации диапазона номеров"
    if start > stop :
        return "Конечное значение не может быть меньше чем начальное значение"


    for number in range(start, stop+1):
        if number <= stop:
            str_number = str(number)
            for num in range(16-len(str_number)):
                str_number = "0" + str_number
                # print(str_number)
            str_num = f"{str_number[0:4]} {str_number[4:7]} {str_number[7:11]} {str_number[-4:]}"
            yield str_num
