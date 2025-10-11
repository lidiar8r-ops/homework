import pytest

from src.decorators import log


def test_log_ok(capsys):
    @log()
    def my_function(x, y):
        return x + y

    my_function(1, 2)
    captured = capsys.readouterr()
    assert captured.out == "my_function ok\n"
 #
 # def test_log_error():
 #    @log()
 #    def my_function(x, y):
 #        return x / y
 #
 #    with pytest.raises(Exception, match="my_function error: (division by zero). Inputs: (1, 0), {}"):
 #        my_function(x, y)

