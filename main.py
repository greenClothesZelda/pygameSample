import pygame
from objects.player import Player

pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
screen: pygame.Surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Entity 표시 예제")

# 엔티티 생성 (asset_path를 None으로 하면 사각형, 이미지 경로를 넣으면 이미지)
player: Player = Player(
    x=100, y=100, width=50, height=50,
    asset_path='assets/_Crouch.png'  # 예: 'assets/character.png'
)

clock: pygame.time.Clock = pygame.time.Clock()
running: bool = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))
    player.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()