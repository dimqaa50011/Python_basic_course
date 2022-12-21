# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на позиции с нечетным индексом.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
from typing import List
from random import randint

from .base_task import BaseTask


class SumElements(BaseTask):
    
    @classmethod
    def run(cls):
        list_numbers = cls.create_list(*cls.get_data())
        elements_in_odd_positions = [list_numbers[i] for i in range(1, len(list_numbers), 2)]
        print(f"{list_numbers} -> на нечётных позициях элементы {', '.join(list(map(str, elements_in_odd_positions)))}, ответ: {cls.get_sum_elements(elements_in_odd_positions)}")

    @staticmethod
    def get_data():
        return (int(input("Введите максимальное значение элемента списка: ")), int(input("Введите длину списка: ")))
    
    @staticmethod
    def create_list(max_value_element: int = 15, length_list: int = 15):
        return [randint(0, max_value_element) for _ in range(length_list)] 

    @staticmethod
    def get_sum_elements(numbers: List) -> int:
        sum_numbers = 0
        for num in numbers:
            sum_numbers += num
        return sum_numbers
