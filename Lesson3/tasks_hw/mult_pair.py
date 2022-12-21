# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]
from random import randint
from typing import List

from .base_task import BaseTask


class MultPair(BaseTask):

    @classmethod
    def run(cls):
        numbers = cls.create_list(*cls.get_data())
        print(f"{numbers} => {cls.get_mult_pair(numbers)}")

    @staticmethod
    def create_list(max_value_element: int = 15, length_list: int = 15):
        return [randint(0, max_value_element) for _ in range(length_list)] 

    @staticmethod
    def get_mult_pair(numbers: List) -> List:
        res_list = []
        length_parity = 1 if len(numbers) % 2 != 0 else 0
        for i in range(len(numbers) // 2 + length_parity):
            res_list.append(numbers[i] * numbers[len(numbers) - i - 1])
        return res_list
    
    @staticmethod
    def get_data():
        return (int(input("Введите максимальное значение элемента списка: ")), int(input("Введите длину списка: ")))
    

