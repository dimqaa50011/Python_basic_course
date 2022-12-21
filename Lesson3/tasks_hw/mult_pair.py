# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]
from random import randint
from typing import List

from .base_task import BaseTask
from .helpers import create_list, get_data


class MultPair(BaseTask):
    @classmethod
    def run(cls):
        numbers = create_list(True, *get_data())
        print(f"{numbers} => {cls.get_mult_pair(numbers)}")

    @staticmethod
    def get_mult_pair(numbers: List) -> List:
        res_list = []
        length_parity = 1 if len(numbers) % 2 != 0 else 0
        for i in range(len(numbers) // 2 + length_parity):
            res_list.append(numbers[i] * numbers[len(numbers) - i - 1])
        return res_list

