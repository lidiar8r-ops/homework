def filter_by_currency(transactions: list[dict], currency: str = 'USD'):
    result = []

    if len(transactions) == 0 or  transactions is None:
        print('Список транзакций пуст')


    for current_dict in transactions:
        try:
            value = current_dict.get("operationAmount").get("currency").get("code")
            if value is None:
                 return "Информация о сумме операции не найдена"
        except:
            return "Информация о сумме операции не найдена"

        for transaction in transactions:
            if transaction.get("operationAmount").get("currency").get("code") == currency:
                yield  transaction
    return  result
