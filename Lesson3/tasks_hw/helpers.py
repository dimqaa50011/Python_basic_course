from random import randint, uniform


def create_list(is_integers: bool, length_list: int = 15, max_value_element: int = 15):
    gen_random = randint if is_integers else uniform
    return [gen_random(0, max_value_element) for _ in range(length_list)]


def get_data():
    return int(input("Введите длину списка: ")), int(input("Введите максимальное значение элемента списка: "))


def round_up(item: float):
    return round(item, 2)
