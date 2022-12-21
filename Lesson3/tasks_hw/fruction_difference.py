# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт 
# разницу между максимальным и минимальным значением дробной части элементов, отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19
from random import uniform
from typing import List, Tuple

from .base_task import BaseTask
from .helpers import create_list, get_data, round_up


class FructionDifference(BaseTask):
    @classmethod
    def run(cls):
        numbers_list = list(map(round_up, create_list(False, *get_data())))
        print(
            f"{numbers_list} => {cls.get_difference(cls.get_max_and_min_elements(cls.get_fractal_parts(numbers_list)))}")

    @classmethod
    def get_fractal_parts(cls, list_numbers: List[float]) -> List[int]:
        return [int(str(el).split(".")[-1]) for el in list_numbers if not el.is_integer()]

    @classmethod
    def get_max_and_min_elements(cls, numbers_list: List[int]) -> Tuple:
        min_element = numbers_list[0]
        max_element = numbers_list[0]

        for number in numbers_list:
            min_element = number if number < min_element else min_element
            max_element = number if number > max_element else max_element

        return tuple(map(lambda item: item / 100, (max_element, min_element)))

    @classmethod
    def get_difference(cls, numbers: Tuple):
        return numbers[0] - numbers[-1]
