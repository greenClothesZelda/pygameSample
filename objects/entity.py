import pygame

from objects.prime.rectangle import Rectangle
from env import isDebug


class Entity(Rectangle):
    def __init__(
            self, x: float, y: float, width: float,
            height: float, color: tuple = (0, 0, 0), angle: float = 0,
            is_display: bool = True, is_active: bool = True, asset_path: str = None):

        super().__init__(x, y, width, height, color, angle)
        self.is_active = is_active
        self.is_display = is_display
        self.asset_path = asset_path
        if asset_path:
            self.image = pygame.image.load(asset_path)
            self.image = pygame.transform.scale(self.image, (int(width), int(height)))
        else:
            self.image = None

    def draw(self, surface):
        if not self.is_active or not self.is_display:
            return
        if self.image:
            surface.blit(self.image, (int(self.x), int(self.y)))
        else:
            super().draw(surface)
        if isDebug:
            # 빨간색 테두리 그리기
            pygame.draw.rect(surface, (255, 0, 0), (int(self.x), int(self.y), int(self.width), int(self.height)), 2)
