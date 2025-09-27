import pytest

from src.masks import get_mask_card_number

"""Функция get_mask_card_number:
1 Тестирование правильности маскирования номера карты.
2 Проверка работы функции на различных входных форматах номеров карт, включая граничные случаи и 
  нестандартные длины номеров.
3 Проверка, что функция корректно обрабатывает входные строки, где отсутствует номер карты."""

@pytest.mark.parametrize(
    "numbers,  expected",
    [
        (7007092289606361, '7007 09** **** 6361'),
        (7000343260636210, '7000 34** **** 6210')
    ],
)
def test_get_mask_card_number(numbers, expected):
    assert get_mask_card_number(numbers) == expected

