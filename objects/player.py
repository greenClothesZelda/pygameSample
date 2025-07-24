from objects.entity import Entity
import pygame
from utils.sprite import get_sprite_frame
from typing import Optional
from objects.properties.moveable import Moveable

class Player(Entity, Moveable):
    def __init__(self, x: float, y: float, width: float, height: float, asset_path: Optional[str] = None) -> None:
        super().__init__(x, y, width, height, color=(0,0,0), asset_path='assets/_Crouch.png')
        self.WALK_SPEED: float = 5.0

        if asset_path:
            self.image: pygame.Surface = get_sprite_frame(asset_path, 42, 48, 32, 32)
            self.image: pygame.Surface = pygame.transform.scale(self.image, (int(width), int(height)))

    def draw(self, surface: pygame.Surface) -> None:
        super().draw(surface)  # 부모 클래스의 draw 메서드를 호출하여 그리기

    def walk_left(self) -> None:
        self.position['dx'] -= self.WALK_SPEED

    def walk_right(self) -> None:
        self.position['dx'] += self.WALK_SPEED
