from datetime import datetime
""" Импортируем метод strptime из модуля datetime"""


class Operation:
    """

    Создаем класс Operation для операций пользователя в банке

    """

    def __init__(self, id_, state, date, operation_amount, description,
                 from_, to):
        self.id = id_
        self.state = state
        self.date = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")
        """ 

        Принимаем строку date и формат даты "%Y-%m-%dT%H:%M:%S.%f", 
        далее — преобразуем в объект datetime с помощью метода .strftime("%d.%m.%Y")

        """
        self.amount = operation_amount.get("amount", "")
        self.currency = operation_amount["currency"].get("name", "")
        self.description = description
        self.from_ = from_
        self.to = to

    def hide_transaction_method_number(self):
        """
                Получаем данные о носителе, с которого была совершена транзакция,
                скрываем его номер определенным способом
                :return: скрытый номер карты/счета
        """
        if self.from_:
            transaction_method_number = ''.join(filter(lambda x: x.isdigit(), self.from_))

            if "Счет" in self.from_:
                hidden_transaction_method_number = f"{self.from_.split()[0]} **{transaction_method_number[-4:]}"
            else:
                card_type = self.from_.replace(transaction_method_number, "").strip()
                hidden_transaction_method_number = (f"{card_type} {transaction_method_number[:4]} "
                                                    f"{transaction_method_number[4:6]}"
                                                    f"{'*' * 2} {'*' * 4} {transaction_method_number[-4:]}")
            return hidden_transaction_method_number
