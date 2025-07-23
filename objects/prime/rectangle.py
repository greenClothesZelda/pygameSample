from objects.prime.shape import Shape
class Rectangle(Shape):
    def __init__(self, x: float, y: float, width: float, height: float, color: tuple = (0, 0, 0), angel: float = 0):
        super().__init__(x, y, color)
        self.width = width
        self.height = height
        self.angel = angel

    def draw(self, surface):
        import pygame
        rect = pygame.Rect(self.x, self.y, self.width, self.height)
        if self.angel != 0:
            rotated_surface = pygame.transform.rotate(surface, self.angel)
            rect = rotated_surface.get_rect(center=rect.center)
            surface.blit(rotated_surface, rect.topleft)
        else:
            pygame.draw.rect(surface, self.color, rect)