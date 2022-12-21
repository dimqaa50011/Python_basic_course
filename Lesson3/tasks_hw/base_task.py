from abc import ABC


class BaseTask(ABC):

    @classmethod
    def run(cls):
        pass
