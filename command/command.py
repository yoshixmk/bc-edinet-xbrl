from abc import abstractmethod, ABCMeta


class Command(metaclass=ABCMeta):
    @abstractmethod
    def execute(self):
        print("execute {} ...".format(self.__class__.__name__))
