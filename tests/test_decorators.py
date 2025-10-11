import pytest

from src.decorators import log


@log()
def my_function(x, y):
    return x + y


def test_log_ok():
        result = my_function(1, 2)
        assert result == "my_function ok"

@log()
def my_function(x, y):
    return x / y


def test_log_error():
    result = my_function(1, 0)
    assert result == "my_function error: (division by zero). Inputs: (1, 0), {}"


name_file = "..\\data4\\mylog.txt"
@log(filename=name_file)
def my_function_del(x, y):
    return x / y


def test_log_error_file():
    with pytest.raises(FileNotFoundError):
        my_function_del(1, 0)





def test_log_ok_file():
    name_file_n = "..\\data\\mylog.txt"
    @log(filename=name_file_n)
    def my_function_test(x, y):
        return x + y

    my_function_test(1, 2)
    with open("..\\data\\mylog.txt", "r", encoding="utf-8") as f:
        text_file = f.read()
    assert "my_function_test ok" in text_file
