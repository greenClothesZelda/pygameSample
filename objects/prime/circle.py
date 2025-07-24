from objects.prime.shape import Shape
import pygame

class Circle(Shape):
    def __init__(self, x: float, y: float, radius: float, color: tuple[int, int, int] = (0, 0, 0)) -> None:
        super().__init__(x, y, color)
        self.radius: float = radius

    def draw(self, surface: pygame.Surface) -> None:
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), int(self.radius))

