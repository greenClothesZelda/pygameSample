from abc import abstractmethod


class PrimeProperty:
    def __init__(self, periority:int)-> None:
        self.__periority = periority

    @abstractmethod
    def execute(self):
        """각 property가 수행할 작업을 정의하는 추상 메서드"""
        pass

    @abstractmethod
    def is_expired(self) -> bool:
        """property가 만료되었는지 여부를 확인하는 추상 메서드"""
        pass

    def get_periority(self) -> int:
        return self.__periority

    def set_periority(self, periority: int) -> None:
        self.__periority = periority