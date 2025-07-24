import pygame

class Shape:
    def __init__(self, x: float, y: float, color: tuple[int, int, int] = (0, 0, 0)) -> None:
        self.x: float = x
        self.y: float = y
        self.color: tuple[int, int, int] = color

    def draw(self, surface: pygame.Surface) -> None:
        raise NotImplementedError("shape is just a base class")