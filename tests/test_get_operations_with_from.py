from develop.utils import get_operations_with_from


def test_get_operations_with_from():
    operations = [
        {"id": 207126257,
         "state": "EXECUTED",
         "date": "2019-07-15T11:47:40.496961",
         "operationAmount": {
             "amount": "92688.46",
             "currency": {
                 "name": "USD",
                 "code": "USD"
             }
         },
         "description": "Открытие вклада",
         "to": "Счет 35737585785074382265"
         },
        {
            "id": 957763565,
            "state": "EXECUTED",
            "date": "2019-01-05T00:52:30.108534",
            "operationAmount": {
                "amount": "87941.37",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 46363668439560358409",
            "to": "Счет 18889008294666828266"
        },
        {
            "id": 893507143,
            "state": "EXECUTED",
            "date": "2018-02-03T07:16:28.366141",
            "operationAmount": {
                "amount": "90297.21",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Открытие вклада",
            "to": "Счет 37653295304860108767"
        }
    ]

    result = get_operations_with_from(operations)

    assert result == [
        {
            "id": 957763565,
            "state": "EXECUTED",
            "date": "2019-01-05T00:52:30.108534",
            "operationAmount": {
                "amount": "87941.37",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 46363668439560358409",
            "to": "Счет 18889008294666828266"
        }
    ]


def test_not_get_operations_with_from():
    operations = [
        {
            "id": 207126257,
            "state": "EXECUTED",
            "date": "2019-07-15T11:47:40.496961",
            "operationAmount": {
                "amount": "92688.46",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Открытие вклада",
            "to": "Счет 35737585785074382265"
        },
        {
            "id": 596171168,
            "state": "EXECUTED",
            "date": "2018-07-11T02:26:18.671407",
            "operationAmount": {
                "amount": "79931.03",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Открытие вклада",
            "to": "Счет 72082042523231456215"
        }
    ]

    result = get_operations_with_from(operations)

    assert result == []
