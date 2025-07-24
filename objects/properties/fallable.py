from objects.properties.prime_property import PrimeProperty

GRAVITY: float = 3
PERIORITY: int = 0  # Fallable의 우선순위

class Fallable(PrimeProperty):
    def __init__(self, position: dict[str:float]):
        super().__init__(PERIORITY)
        self.position: dict[str: float] = position
        self.__gravity: float = GRAVITY

    def execute(self) -> None:
        self.position['dy'] += self.__gravity

    def get_gravity(self) -> float:
        return self.__gravity

    def set_gravity(self, gravity: float) -> None:
        self.__gravity = gravity

