# Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0
# и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
#
# Пример:
#
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

def get_quarter(x: int, y: int) -> int:
    quarter: int
    if x > 0 and y > 0:
        quarter = 1
    elif x > 0 and y < 0:
        quarter = 4
    elif x < 0 and y > 0:
        quarter = 2
    else:
        quarter = 3
    return quarter


def run_task2():
    print(f'Четверть номер {get_quarter(int(input("Введите коортинату X: ")), int(input("Введите координату  Y: ")))}')
