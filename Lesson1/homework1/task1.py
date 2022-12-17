# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет,
# является ли этот день выходным.
#
# Пример:
#
# - 6 -> да
# - 7 -> да
# - 1 -> нет

def is_weekend(day: int) -> bool:
    return 6 <= day <= 7


def run_task1():
    msg: str
    if is_weekend(int(input("Введите день недели: "))):
        msg = "Да"
    else:
        msg = "Нет"
    print(msg)