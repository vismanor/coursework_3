import json
""" Импортируем бибилиотеку для работы с json файлом"""
from operation_class import Operation


def load_data(filename):
    with open(filename, 'r', encoding='UTF-8') as file:
        """ 

        Открываем json файл для чтения 

        """
        data = json.load(file)
        return data


def get_executed_operations(data):
    """
            Фильтруем все операции, чтобы получить только со статусом 'executed'
    """
    return [operation for operation in data if "state" in operation and operation["state"] == "EXECUTED"]


def get_operations_with_from(operations):
    """
                Фильтруем все операции, чтобы получить только с пунктом 'from'
    """
    return [operation for operation in operations if "from" in operation]
