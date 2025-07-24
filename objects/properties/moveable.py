from objects.properties.prime_property  import PrimeProperty

PERIORITY = 0

class Moveable(PrimeProperty):
    def __init__(self, position:dict[str:float]) -> None:
        """
        Initialize the Moveable property with a given priority.

        :param priority: The priority of the Moveable property.
        """
        super().__init__(PERIORITY)
        self.position: dict[str: float] = position

    def execute(self) -> None:
        """
        Update the position based on the current velocity.
        """
        self.position['x'] += self.position['dx']
        self.position['y'] += self.position['dy']
        self.position['dx'] = 0
        self.position['dy'] = 0