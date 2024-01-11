from develop.utils import get_last_five_operations


def test_get_last_five_operations():
    operations_with_from = [
        {"date": "2022-01-01"},
        {"date": "2022-01-02"},
        {"date": "2022-01-03"},
        {"date": "2022-01-04"},
        {"date": "2022-01-05"},
        {"date": "2022-01-06"}
    ]

    result = get_last_five_operations(operations_with_from, 5)

    assert (sorted(result, key=lambda x: x["date"], reverse=True) ==
            sorted(operations_with_from[-5:], key=lambda x: x["date"], reverse=True))


def test_get_last_five_but_not_five_operations():
    operations_with_from = [
        {"date": "2022-01-01"},
        {"date": "2022-01-02"},
        {"date": "2022-01-03"},
        {"date": "2022-01-04"},
        {"date": "2022-01-05"},
        {"date": "2022-01-06"}
    ]

    result = get_last_five_operations(operations_with_from, 3)

    assert (sorted(result, key=lambda x: x["date"], reverse=True) ==
            sorted(operations_with_from[-3:], key=lambda x: x["date"], reverse=True))


def test_get_empty_operations():
    operations_with_from = []

    result = get_last_five_operations(operations_with_from, 5)

    assert result == []


def test_get_last_five_operations_from_smaller_list():
    operations_with_from = [
        {"date": "2022-01-01"},
        {"date": "2022-01-02"},
        {"date": "2022-01-03"}
    ]

    result = get_last_five_operations(operations_with_from, 5)

    assert (sorted(result, key=lambda x: x["date"], reverse=True) ==
            sorted(operations_with_from[-3:], key=lambda x: x["date"], reverse=True))
