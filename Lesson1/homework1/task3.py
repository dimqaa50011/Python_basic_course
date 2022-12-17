# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

def run_task3():
    quarter = int(input("Введите номер четверти: "))
    print(f"Диапазон возможных точек для четверти {quarter} = {get_interval_available_values_for_points(quarter)}")


def get_interval_available_values_for_points(quarter: int) -> str:
    result: str
    if quarter == 1:
        result = "X > 0; Y > 0"
    elif quarter == 2:
        result = "X < 0; Y > 0"
    elif quarter == 3:
        result = "X < 0; Y < 0"
    else:
        result = "X > 0; Y < 0"

    return result
