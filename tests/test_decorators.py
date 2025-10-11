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

