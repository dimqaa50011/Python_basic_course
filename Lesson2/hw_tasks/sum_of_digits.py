# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11


class SumDigits:
    
    def run(self):
        self.number = float(input("Введите вещественное число: ").replace(",", "."))
        print(f"{self.number} -> {self.from_string()}")
        
    
    def from_string(self):
        return self._get_sum_digits(int(str(self.number).replace(".", "")))
    

    @staticmethod
    def _get_sum_digits(num: int) -> int:
        sum_digits = 0
        while num > 0:
            sum_digits += num % 10
            num //= 10
        return sum_digits
