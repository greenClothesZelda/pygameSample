import pygame
from typing import Optional

from objects.prime.rectangle import Rectangle
from env import isDebug


class Entity(Rectangle):
    def __init__(
            self, x: float, y: float, width: float,
            height: float, color: tuple[int, int, int] = (0, 0, 0), angle: float = 0,
            is_display: bool = True, is_active: bool = True, asset_path: Optional[str] = None) -> None:

        super().__init__(x, y, width, height, color, angle)
        self.is_active: bool = is_active
        self.is_display: bool = is_display
        self.asset_path: Optional[str] = asset_path
        self.image: Optional[pygame.Surface] = None
        if asset_path:
            self.image = pygame.image.load(asset_path)
            self.image = pygame.transform.scale(self.image, (int(width), int(height)))

    def draw(self, surface: pygame.Surface) -> None:
        if not self.is_active or not self.is_display:
            return
        if self.image:
            surface.blit(self.image, (int(self.position['x']), int(self.position['y'])))
        else:
            super().draw(surface)
        if isDebug:
            # 빨간색 테두리 그리기
            pygame.draw.rect(surface, (255, 0, 0), (int(self.position['x']), int(self.position['y']), int(self.width), int(self.height)), 2)