from develop.utils import get_executed_operations


def test_get_executed_operations():
    data = [
        {"state": "EXECUTED", "id": 441945886},
        {"state": "EXECUTED", "id": 41428829},
        {"state": "CANCELED", "id": 970724427},
    ]
    result = get_executed_operations(data)

    assert result == [
        {"state": "EXECUTED", "id": 441945886},
        {"state": "EXECUTED", "id": 41428829},
    ]


def test_not_get_executed_operations():
    data = [
        {"state": "CANCELED", "id": 608117766},
        {"state": "CANCELED", "id": 970724427},
    ]
    result = get_executed_operations(data)

    assert result == []
