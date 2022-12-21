from typing import List

# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи
from .base_task import BaseTask


class Fibonacci(BaseTask):
    @classmethod
    def run(cls):
        print(cls.get_fibonacci(int(input("Введите длину последовательности: "))))

    @classmethod
    def show_condition(cls):
        print("Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.\n")

    @classmethod
    def get_fibonacci(cls, length: int):
        fibonacci_seq = [1, 1]
        nega_fibonacci_seq = [1, -1]

        for i in range(2, length):
            fibonacci_seq.append(fibonacci_seq[i - 1] + fibonacci_seq[i - 2])

        for i in range(2, length):
            nega_fibonacci_seq.append(nega_fibonacci_seq[i - 2] - nega_fibonacci_seq[i - 1])

        return cls.get_result(fibonacci_seq, nega_fibonacci_seq)

    @classmethod
    def get_result(cls, fibonacci_seq: List, nega_fibonacci_seq: List):
        return ", ".join(tuple(map(str, (list(reversed(nega_fibonacci_seq)) + [0] + list(fibonacci_seq)))))