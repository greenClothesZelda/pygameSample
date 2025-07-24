from objects.prime.shape import Shape
import pygame

class Rectangle(Shape):
    def __init__(self, x: float, y: float, width: float, height: float, color: tuple[int, int, int] = (0, 0, 0), angel: float = 0) -> None:
        super().__init__(x, y, color)
        self.width: float = width
        self.height: float = height
        self.angel: float = angel

    def draw(self, surface: pygame.Surface) -> None:
        rect = pygame.Rect(self.position['x'], self.position['y'], self.width, self.height)
        if self.angel != 0:
            # Create a new surface with the same size as the rectangle
            rotated_surface = pygame.Surface((rect.width, rect.height), pygame.SRCALPHA)
            # Draw the rectangle onto the new surface
            pygame.draw.rect(rotated_surface, self.color, (0, 0, rect.width, rect.height))
            # Rotate the new surface
            rotated_surface = pygame.transform.rotate(rotated_surface, self.angel)
            # Get the new rect of the rotated surface
            rect = rotated_surface.get_rect(center=rect.center)
            # Blit the rotated surface onto the main surface
            surface.blit(rotated_surface, rect.topleft)
        else:
            pygame.draw.rect(surface, self.color, rect)

    def get_min_x(self) -> float:
        return self.position['x']
    def get_max_x(self) -> float:
        return self.position['x'] + self.width
    def get_min_y(self) -> float:
        return self.position['y']
    def get_max_y(self) -> float:
        return self.position['y'] + self.height