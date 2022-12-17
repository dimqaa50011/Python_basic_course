# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
#
# Пример:
#
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

def run_task4():
    points = []
    for i in range(4):
        points.append(int(input(f"Введите координату номер {i + 1}: ")))

    print(
        f"A({points[0]},{points[1]}); B({points[2]},{points[3]}) -> {get_distance(tuple(points[:2]), tuple(points[2:]))}")


def get_distance(point_a: tuple, point_b: tuple) -> float:
    return (((point_b[0] - point_a[0]) ** 2) + ((point_b[-1] - point_a[-1]) ** 2)) ** 0.5
