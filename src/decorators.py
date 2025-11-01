# Этот модуль будет использоваться для размещения декораторов
# Ожидаемый вывод в лог-файл mylog.txt
# при успешном выполнении:  my_function ok
# Ожидаемый вывод при ошибке: my_function error: тип ошибки. Inputs: (1, 2), {}
# Где тип ошибки заменяется на текст ошибки.
import logging
import os
from datetime import datetime
from functools import wraps
from typing import Any, Callable

# Получаем директорию текущего файла (т.е. папку src)
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
# Формируем абсолютный путь к папке log (которая находится на уровень выше)
LOG_DIR = os.path.join(CURRENT_DIR, "..", "logs")
log_file_path = os.path.join(LOG_DIR, "decorators.log")

# Настройка логирования
logger_decorators = logging.getLogger("decorators")
file_handler_decorators = logging.FileHandler(log_file_path, "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler_decorators.setFormatter(file_formatter)
logger_decorators.addHandler(file_handler_decorators)
logger_decorators.setLevel(logging.DEBUG)


def log(filename: str = "") -> Callable[..., Any]:
    """декоратор, который  автоматически логирует начало и конец выполнения функции, а также ее результаты или
    возникшие ошибки.Декоратор должен принимать необязательный аргумент filename, который определяет, куда будут
    записываться логи (в файл или в консоль):
    Если filename задан, логи записываются в указанный файл.
    Если filename не задан, логи выводятся в консоль."""

    def decorator_log(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            current_time_start = datetime.now().time()

            try:
                result = func(*args, **kwargs)
                current_time_stop = datetime.now().time()
                result_bool = "ok"
                str_result_2 = f"{func.__name__} {result_bool}"
            except Exception as e:
                result_bool = f"error: ({e})"
                current_time_stop = datetime.now().time()
                str_result_2 = f"{func.__name__} {result_bool}. Inputs: {args}, {kwargs}"

            str_result_1 = f"\nНачало выполнения функции : {current_time_start}\n"
            str_result_3 = f"\nвремя завершения работы функции {current_time_stop}"

            if filename == "":
                print(str_result_1)
                print(str_result_2)
                print(str_result_3)

            else:
                try:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(str_result_1)
                        file.write(str_result_2)
                        file.write(str_result_3)
                except FileNotFoundError as e:
                    raise FileNotFoundError(e)
            if "error" in result_bool:
                raise ValueError(result_bool)
            return result

        return wrapper

    return decorator_log
