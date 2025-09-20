def filter_by_state(input_list: list[dict], state = 'EXECUTED') -> list:
    """
    функция принимает список словарей и опционально значение для ключа state.
    Функция возвращает новый список словарей, содержащий только те словари, у которых ключ state соответствует
    указанному значению.
    :param input_list:  список словарей
    :param state: опционально значение для ключа state, по умолчанию 'EXECUTED'
    """
    return  [n_dict for n_dict in input_list if n_dict['state'] == state]


lists = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
     {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
     {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
     {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

print(filter_by_state(lists, 'CANCELED'))