from objects.properties.prime_property import PrimeProperty

PERIORITY: int = -1  # Fallable의 우선순위

class Jump(PrimeProperty):
    def __init__(self, position: dict[str:float], power: float = 20, gravity: float = 1):
        super().__init__(PERIORITY)
        self.position: dict[str: float] = position
        self.power: float = power
        self.__gravity: float = gravity

    def execute(self) -> None:
        if self.position['dy'] == 0:
            self.position['dy'] = -self.power
            self.power -= self.__gravity

    def is_expired(self) -> bool:
        return self.power <= 0

