from objects.entity import Entity
import pygame
from utils.sprite import get_sprite_frame
from typing import Optional

class Player(Entity):
    def __init__(self, x: float, y: float, width: float, height: float, asset_path: Optional[str] = None) -> None:
        super().__init__(x, y, width, height, color=(0,0,0), asset_path='assets/_Crouch.png')
        self.health: int = 100  # 플레이어의 초기 체력
        self.score: int = 0     # 플레이어의 초기 점수
        # 예시: 캐릭터가 (x=32, y=32) 위치에 있고 크기가 32x32라면
        if asset_path:
            self.image: pygame.Surface = get_sprite_frame(asset_path, 42, 48, 32, 32)
            self.image: pygame.Surface = pygame.transform.scale(self.image, (int(width), int(height)))

    def draw(self, surface: pygame.Surface) -> None:
        super().draw(surface)  # 부모 클래스의 draw 메서드를 호출하여 그리기