from homework1.task1 import is_weekend


def main():
    msg: str
    if is_weekend(int(input("Введите день недели: "))):
        msg = "Да"
    else:
        msg = "Нет"
    print(msg)


if __name__ == '__main__':
    main()
