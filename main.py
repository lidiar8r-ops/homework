import json
import os
import logging

from src.config import DATA_DIR
from src.generators import filter_by_currency
from src.get_csv_xls import get_csv_xlsx_reader_transaction
from src.list_operations import process_bank_search

from src.processing import filter_by_state, sort_by_date
from src.utils import get_list_transaction, get_list_operation
from src.widget import get_date, mask_account_card

# Получаем директорию текущего файла (т.е. папку src)
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
# Формируем абсолютный путь к папке log (которая находится на уровень выше)
LOG_DIR = os.path.join(CURRENT_DIR,  'logs')
log_file_path = os.path.join(LOG_DIR, 'main.log')

# Настройка логирования
logger_main = logging.getLogger("main")
file_handler_main = logging.FileHandler(log_file_path, "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler_main.setFormatter(file_formatter)
logger_main.addHandler(file_handler_main)
logger_main.setLevel(logging.DEBUG)

# DATA_DIR = os.path.join(CURRENT_DIR,'data')

def main() ->str:
    """ Функция отвечает за основную логику проекта и связывает функциональности между собой.
    1. Выбор файла для получения информации из него
    2. Выбор статуса, по которому необходимо выполнить фильтрацию
    3.
    """
    str_result: str = ''
    try:
        logger_main.info("Начало работы программы")
        # Выбор файла для получения информации из него
        get_num = int(input('Привет! Добро пожаловать в программу работы с банковскими транзакциями.\n'
                            'Выберите необходимый пункт меню:\n'
                            '1. Получить информацию о транзакциях из JSON-файла\n'
                            '2. Получить информацию о транзакциях из CSV-файла\n'
                            '3. Получить информацию о транзакциях из XLSX-файла\n'))

        if get_num == 1:
            print("Для обработки выбран JSON-файл.")

        elif get_num == 2:
            print("Для обработки выбран CSV-файл.")

        elif get_num == 3:
            print("Для обработки выбран XLSX-файл.")

        else:
            return 'Введено не корректное значение'

    except Exception as e:
        return 'Введено не корректное значение'

    inp_state = ''
    # ВРЕМЕННО
    inp_state = inp_state.upper()
    # inp_state = 'EXECUTED'
    while not inp_state == 'EXECUTED' or  not inp_state == 'CANCELED' or not inp_state == 'PENDING':
        inp_state = input('Введите статус, по которому необходимо выполнить фильтрацию.\n'
                          'Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n')
        # ВРЕМЕННО
        inp_state = inp_state.upper()
        # inp_state = 'EXECUTED'

        # Выбор статуса, по которому необходимо выполнить фильтрацию
        if inp_state == 'EXECUTED' or inp_state == 'CANCELED' or inp_state == 'PENDING':
            print(f'Операции отфильтрованы по статусу "{inp_state}"')
            break
        else:
           print(f'Статус операции "{inp_state}" недоступен.')

    # Выборка сортировки и фильтрации
    inp_date = input('Отсортировать операции по дате? Да/Нет ')
    # inp_date ='Да'
    if inp_date.upper() == 'ДА':
        flag_date = True
        inp_sort = input('Отсортировать по возрастанию или по убыванию? ')
        if inp_sort.upper() in 'ПО ВОЗРАСТАНИЮ':
            flag_sort = False
        else:
            flag_sort = True
    else:
        flag_date= False

    inp_code = input('Выводить только рублевые транзакции? Да/Нет')
    if inp_code.upper() == 'ДА':
        flag_code = True
    else:
        flag_code = False

    inp_word = input('Отфильтровать список транзакций по определенному слову в описании? Да/Нет')
    if inp_word.upper() == 'ДА':
        inp_description = input('Введите определенное слово в описании').upper()
    else:
        inp_description = ''

    # Начало формирования итогового списка транзакий
    logger_main.info("Начало формирования итогового списка транзакий...")
    print('Распечатываю итоговый список транзакций...')

    # Если для обработки выбран JSON-файл
    if get_num == 1:
        logger_main.info("Получаем данные из JSON-файла")
        list_transaction = get_list_transaction(os.path.join(DATA_DIR, 'operations.json'))

    # Если для обработки выбран CSV-файл
    elif get_num == 2:
        logger_main.info("Получаем данные из CSV-файла")
        list_transaction = get_csv_xlsx_reader_transaction(os.path.join(DATA_DIR, 'transactions.csv'))

    # Если для обработки выбран XLSX-файл
    else:
        logger_main.info("Получаем данные из XLSX-файла")
        list_transaction = get_csv_xlsx_reader_transaction(os.path.join(DATA_DIR, 'transactions_excel.xlsx'))

    logger_main.info(f'фильтруем список словарей по значение ключа {inp_state} и возвращаем новый список словарей')
    # фильтруем список словарей по значение ключа inp_state и возвращаем новый список словарей
    list_transaction = filter_by_state(list_transaction, inp_state)

    if flag_date:
        logger_main.info('возвращаем список словарей, отсортированный по дате')
        # возвращаем список словарей, отсортированный по дате
        list_transaction = sort_by_date(list_transaction, flag_sort)

    if flag_code:
        logger_main.info('возвращаем список словарей, с только рублевыми операциями')
        # возвращаем список словарей, с только рублевыми операциями = Фильтрация по RUB
        list_transaction =list(filter_by_currency(list_transaction, "RUB"))

    if inp_word.upper() == 'ДА':
        logger_main.info(f'возвращаем список словарей, со строкой поиска <<{inp_description}>> в описании')
        # возвращаем список словарей, со строкой поиска в описании
        list_transaction = process_bank_search(list_transaction, inp_description)

    logger_main.info("Вывод в консоль полученную выборку")
    if list_transaction == [] or list_transaction == None:
        logger_main.info("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        logger_main.info(f"Всего банковских операций в выборке: {len(list_transaction)}")
        print(f"Всего банковских операций в выборке: {len(list_transaction)}\n")
        for transaction in list_transaction:
            date_transaction = get_date(str(transaction.get("date", "")))
            description_transaction = transaction.get("description", "")
            from_account_transaction = mask_account_card(transaction.get("from", ""))
            to_account_transaction = mask_account_card(transaction.get("to", ""))
            amount_transaction = transaction.get("operationAmount","").get("amount","")
            currency_transaction = transaction.get("currency","")
            code_transaction = transaction.get("operationAmount","").get("currency","").get("name", "")

            print(f"{date_transaction} {description_transaction}")
            if from_account_transaction and to_account_transaction:
                print(f"{from_account_transaction} -> {to_account_transaction}")
            elif from_account_transaction:
                print(f"{from_account_transaction}")
            print(f"Сумма: {amount_transaction} {currency_transaction} {code_transaction}\n")

        logger_main.info("Завершение работы программы")

    return str_result


if __name__ == '__main__':
    main()
