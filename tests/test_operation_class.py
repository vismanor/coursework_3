from operation_class import Operation


def test_operation_init():
    op = Operation(id_=1, state="EXECUTED", date="2022-01-01T12:00:00.000",
                   operation_amount={"amount": 100, "currency": {"name": "USD"}},
                   description="Test", from_="Visa Gold 1234 5678 9101 1121",
                   to="Счет 1456 1111 2222 2233 4455")
    assert op.id == 1
    assert op.state == "EXECUTED"
    assert op.date == "01.01.2022"
    assert op.amount == 100
    assert op.currency == "USD"
    assert op.description == "Test"
    assert op.from_ == "Visa Gold 1234 5678 9101 1121"
    assert op.to == "Счет 1456 1111 2222 2233 4455"


def test_hide_account_number():
    op = Operation(id_=1, state="EXECUTED", date="2022-01-01T12:00:00.000",
                   operation_amount={"amount": 100, "currency": {"name": "USD"}},
                   description="Test", from_="Visa Gold 1234 5678 9101 1121",
                   to="Счет 1456 1111 2222 2233 4455")
    hidden_number = op.hide_account_number()
    assert hidden_number == "Счет **4455"
