from tasks_hw import BaseTask


def runner():
    task_number = 1
    for task in BaseTask.__subclasses__():
        print(f"Задача номер {task_number}")
        task.run()
        task_number += 1
        print("_" * 50)


if __name__ == "__main__":
    runner()
