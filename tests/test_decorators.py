import pytest


def test_log_error():
    @log()
    def my_function(x, y):
        return x + y

    result = add_numbers(1, 2)
    assert result == "my_function ok."
# my_function(1, 0)
#     with pytest.raises(Exception, match="Max retries exceeded"):
#         my_function(x, y)

# ---


def double_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * 2
    return wrapper


def add_numbers(a, b):
    return a + b

def test_double_decorator():
    @double_decorator
    def add_numbers(a, b):
        return a + b

    result = add_numbers(3, 5)
    assert result == 16  # (3 + 5) * 2
