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
