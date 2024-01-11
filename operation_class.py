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
