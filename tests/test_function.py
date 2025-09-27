import pytest

from src.masks import get_mask_card_number

# """Функция get_mask_card_number:
# 1 Тестирование правильности маскирования номера карты.
# 2 Проверка работы функции на различных входных форматах номеров карт, включая граничные случаи и
#   нестандартные длины номеров.
# 3 Проверка, что функция корректно обрабатывает входные строки, где отсутствует номер карты."""

@pytest.mark.parametrize(
    "numbers,  expected",
    [
        (7007092289606361, '7007 09** **** 6361'),
        (7000343260636210, '7000 34** **** 6210')
    ],
)
def test_get_mask_card_number(numbers, expected):
    assert get_mask_card_number(numbers) == expected


@pytest.mark.parametrize(
    "numbers",
    [(70070922896063261),
     (770070922896063261),
     (70003432606362)]
)
def test_get_mask_card_number_correct_len(numbers):
    with pytest.raises(ValueError):
        get_mask_card_number(numbers)


@pytest.mark.parametrize(
    "numbers",
    [(77007092289606.3),
    (0000000000000000),
    ('7700709228960632')]
)
def test_get_mask_card_number_correct_type(numbers):
    with pytest.raises(TypeError):
        get_mask_card_number(numbers)


@pytest.mark.parametrize(
    "numbers",
    [( ),
     (0)]
)
def test_get_mask_card_number_correct_empty(numbers):
    with pytest.raises(TypeError):
        get_mask_card_number(numbers)
