# from tasks_hw.fibonacci import Task5
from tasks_hw import BaseTask


def runner():
    print(BaseTask.__subclasses__())
    print()

    for task in BaseTask.__subclasses__():
        task.run()


if __name__ == "__main__":
    runner()
