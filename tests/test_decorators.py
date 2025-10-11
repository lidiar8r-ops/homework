import pytest

from src.decorators import log


@log()
def my_function(x, y):
    return x + y


def test_log_ok():
    result = my_function(1, 2)
    assert result == "my_function ok"


@log()
def my_function_delete(x, y):
    return x / y


def test_log_error():
    result = my_function_delete(1, 0)
    assert result == "my_function_delete error: (division by zero). Inputs: (1, 0), {}"


name_file = r"data4\mylog.txt"


@log(filename=name_file)
def my_function_del(x, y):
    return x / y


def test_log_error_file():
    with pytest.raises(FileNotFoundError):
        my_function_del(1, 0)


def test_log_ok_file():
    name_file_n = r"data\mylog.txt"

    @log(filename=name_file_n)
    def my_function_test(x, y):
        return x + y

    my_function_test(1, 2)
    with open(r"data\mylog.txt", "r", encoding="utf-8") as f:
        text_file = f.read()
    assert "my_function_test ok" in text_file


@log()
def my_function_no_args():
    return "No arguments"


def test_my_function_no_args():
    result = my_function_no_args()
    assert result == "my_function_no_args ok"


@log()
def my_function_kwargs(x, y, str_kwargs="5"):
    return x + y, str_kwargs


def test_my_function_kwargs():
    result = my_function_kwargs()
    assert result == (
        "my_function_kwargs error: (my_function_kwargs() missing 2 required "
        "positional arguments: 'x' and 'y'). Inputs: (), {}"
    )
