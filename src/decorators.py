#Этот модуль будет использоваться для размещения декораторов
# Ожидаемый вывод в лог-файл mylog.txt
# при успешном выполнении:  my_function ok
# Ожидаемый вывод при ошибке: my_function error: тип ошибки. Inputs: (1, 2), {}
# Где тип ошибки заменяется на текст ошибки.
from datetime import datetime
from functools import  wraps


def log(filename=''):
    def decorator_log(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            current_time_start = datetime.now().time()

            try:
                result = func(*args, **kwargs)
                current_time_stop = datetime.now().time()
                result_bool = 'ok'
                str_result_2 = f'{func.__name__} {result_bool}'
            except Exception as e:
                result_bool = f"error: ({e})"
                current_time_stop = datetime.now().time()
                str_result_2 = f'{func.__name__} {result_bool}. Inputs: {args}, {kwargs}'


            # str_result = f'Начало выполнения функции : {current_time_start}\n{func.__name__} {result_bool}. Inputs: {args}, {kwargs} \nвремя завершения работы функции {current_time_stop}'
            str_result_1 = f'\nНачало выполнения функции : {current_time_start}\n'
            str_result_3 = f'\nвремя завершения работы функции {current_time_stop}'

            if filename == '':
                # print(str_result_1)
                print(str_result_2)
                # print(str_result_3)
            else:
                with open(filename, 'a', encoding='utf-8') as file:
                    file.write(str_result_1)
                    file.write(str_result_2)
                    file.write(str_result_3)
        return wrapper
    return decorator_log
#
#
# @log(filename="..\\data\\mylog.txt")
# def my_function(x, y):
#     return x / y
#
# my_function(1, 0)