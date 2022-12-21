# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

from .base_task import BaseTask


class ConvertToBinary(BaseTask):
    @classmethod
    def run(cls):
        number = int(input("Введите число: "))
        print(f"{number} -> {cls.get_binary(number)}")

    @classmethod
    def show_condition(cls):
        print("Напишите программу, которая будет преобразовывать десятичное число в двоичное.\n")

    @classmethod
    def get_binary(cls, number: int):
        bin_list = []
        while number > 0:
            bin_list.append(number % 2)
            number //= 2
        return int("".join(tuple(map(str, reversed(bin_list)))))
