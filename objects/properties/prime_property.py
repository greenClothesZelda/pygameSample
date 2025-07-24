from abc import abstractmethod


class PrimeProperty:
    def __init__(self, periority:int)-> None:
        self.__periority = periority

    @abstractmethod
    def execute(self):
        pass

    def get_periority(self) -> int:
        return self.__periority

    def set_periority(self, periority: int) -> None:
        self.__periority = periority