# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на позиции с нечетным индексом.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
from typing import List
from random import randint

from .base_task import BaseTask
from .helpers import create_list, get_data


class SumElements(BaseTask):

    @classmethod
    def run(cls):
        list_numbers = create_list(True, *get_data())
        elements_in_odd_positions = [list_numbers[i] for i in range(1, len(list_numbers), 2)]
        print(f"{list_numbers} -> на нечётных позициях элементы "
              f"{', '.join(list(map(str, elements_in_odd_positions)))}"
              f", ответ: {cls.get_sum_elements(elements_in_odd_positions)}")

    @classmethod
    def show_condition(cls):
        print("Задайте список из нескольких чисел. Напишите программу,\n"
              "которая найдёт сумму элементов списка, стоящих на позиции с нечетным индексом.\n")

    @staticmethod
    def get_sum_elements(numbers: List) -> int:
        sum_numbers = 0
        for num in numbers:
            sum_numbers += num
        return sum_numbers
