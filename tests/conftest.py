import pytest


# Создаем фикстуру, которая запускается перед каждым тестом
@pytest.fixture
def test_lists() -> list:  # Имя фикстуры — любое
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


# Создаем фикстуру, которая запускается перед каждым тестом
@pytest.fixture
def test_lists_date_similar() -> list:  # Имя фикстуры — любое
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226726, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def test_lists_no_correct_key() -> list:  # Имя фикстуры — любое
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state1": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date1": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "30-01-2018T02:08:58.425572"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def test_lists_no_correct_date() -> list:  # Имя фикстуры — любое
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019.23.03"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-07-30"},
        {"id": 594226726, "state": "CANCELED", "date": "2018/09/12T21:27:25.241689"},
        {"id": 594226727, "state": "CANCELED", "date": None},
        {"id": 594226727, "state": "CANCELED", "date": ""},
        {"id": 939719570, "state": "EXECUTED", "date": "2018.06.30T02:08:58.425572"},
        {"id": 615064591, "state": "CANCELED", "date": "2018"},
    ]


@pytest.fixture
def test_lists_no_correct_no_date() -> list:  # Имя фикстуры — любое
    return [
        {"id": 939719570, "state": "EXECUTED", "date": 2018.101},
        {"id": 939719570, "state": "EXECUTED", "date": True},
        {"id": 939719570, "state": "EXECUTED", "date": None},
        {"id": 939719570, "state": "EXECUTED", "date": ()},
        {"id": 939719570, "state": "EXECUTED", "date": 0},
    ]
