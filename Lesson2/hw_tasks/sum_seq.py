from typing import List
# Задайте список из n чисел последовательности (1 + 1/n)**n, выведеите его на экран, а так же сумму элементов списка.
# Пример:
# Для n=4 -> [2, 2.25, 2.37, 2.44]
# Сумма 9.06


class SeqNumbers:

    def run(self):
        len_seq = int(input("Введите длину списка: "))
        seq_nums = self.generation_list(len_seq)
        print(f"Для n={len_seq} -> {seq_nums}\nСумма {self.get_sum_seq(seq_nums)}")

    def generation_list(self, length_list: int):
        return [round(self.get_element(item + 1), 2) for item in range(length_list)]

    @staticmethod
    def get_element(num: int) -> int:
        return (1 + 1/num) ** num
    
    @staticmethod
    def get_sum_seq(seq_nums: List[float]):
        sum_seq = 0
        for num in seq_nums:
            sum_seq += num
        return sum_seq


