# Реализуйте алгоритм перемешивания списка. НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE,
# максимум использование библиотеки Random для получения случайного int
from typing import List
from random import randint


class ShufflingList:
    def run(self):
        list_numbers = self.get_list_random_numbers(left_border=0, right_border=15, max_length=15)
        print(f"Исходный список: {list_numbers}")
        print(f"Пермешанный список: {self.list_shuffling(list_numbers)}")
    
    @staticmethod
    def get_list_random_numbers(left_border: int, right_border: int, max_length: int) -> List:
        return [randint(left_border, right_border) for _ in range(max_length)]

    @classmethod
    def list_shuffling(cls, list_numbers: List):
        if len(list_numbers) == 1:
            return list_numbers
        item = [list_numbers.pop(randint(0, len(list_numbers) - 1))]
        return item + cls.list_shuffling(list_numbers) 
        