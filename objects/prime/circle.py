from objects.prime.shape import Shape

class Circle(Shape):
    def __init__(self, x: float, y: float, radius: float, color: tuple = (0, 0, 0)):
        super().__init__(x, y, color)
        self.radius = radius

    def draw(self, surface):
        import pygame
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), int(self.radius))

