import os

from src.decorators import log

@log()
def my_function(x, y):
    return x + y


def test_log_ok(capsys):
    my_function(1, 2)
    captured = capsys.readouterr()
    assert captured.out == "my_function ok"

def test_log_error(capsys):
    my_function(1, 2)
    captured = capsys.readouterr()
    assert captured.out == "my_function error: (division by zero). Inputs: (1, 0), {}"


name_file = ("..\\data\\mylog.txt"
@log(filename=name_file))
def my_function_del(x, y):
    return x / y


def test_log_ok_file(capsys):
    my_function(1, 2)
    # name_file = "..\\data\\mylog.txt"

    name_dir = os.path.dirname(os.path.dirname(__file__).rstrip("/"))

    name_file = os.path.join(name_dir, "data", 'mylog.txt')
    print(name_file)
    # with open(name_file, "r") as f:
    #     text_file = f.read()
    assert "my_function ok" in text_file

#
# @log(filename="..\\data\\mylog.txt")
# def my_function(x, y):
#     return x / y
#
# my_function(1, 0)
