from objects.entity import Entity
import pygame

class Player(Entity):
    def __init__(self, x, y, width, height, asset_path=None):
        super().__init__(x, y, width, height, color=(0,0,0), asset_path='assets/_Crouch.png')
        self.health = 100  # 플레이어의 초기 체력
        self.score = 0     # 플레이어의 초기 점수
        full_image = pygame.image.load(asset_path).convert_alpha()
        # 예시: 캐릭터가 (x=32, y=32) 위치에 있고 크기가 32x32라면
        char_rect = pygame.Rect(42, 48, 32, 32)
        self.image = full_image.subsurface(char_rect).copy()
        self.image = pygame.transform.scale(self.image, (int(width), int(height)))

    def draw(self, surface):
        super().draw(surface)  # 부모 클래스의 draw 메서드를 호출하여 그리기