import pygame

class Shape:
    def __init__(self, x: float, y: float, color: tuple[int, int, int] = (0, 0, 0), is_moveable:bool = False) -> None:
        self.position: dict[str:float] = {'x': x, 'y': y, 'dx': 0.0, 'dy': 0.0}
        self.color: tuple[int, int, int] = color
        self.is_moveable: bool = is_moveable

    def draw(self, surface: pygame.Surface) -> None:
        raise NotImplementedError("shape is just a base class")

    def move(self) -> None:
        self.position['x'] += self.position['dx']
        self.position['y'] += self.position['dy']
        self.position['dx'] = 0
        self.position['dy'] = 0