import pygame
from objects.entity import Entity
from objects.player import Player
from enum import Enum
import heapq
import copy

from objects.properties.fallable import Fallable
from objects.properties.moveable import Moveable
from objects.block import Block


class DrawOrder(Enum):
    BACKGROUND = 0
    ENTITY = 1
    FOREGROUND = 2

def draw_all(screen , object_list, background_tile):
    tile_width, tile_height = background_tile.get_size()
    # 배경 타일 반복 출력
    for y in range(0, screen.get_height(), tile_height):
        for x in range(0, screen.get_width(), tile_width):
            screen.blit(background_tile, (x, y))
    # 얕은 복사로 임시 큐 생성
    temp_list = object_list[:]
    while temp_list:
        priority, obj = heapq.heappop(temp_list)
        if hasattr(obj, "draw"):
            obj.draw(screen)

def update_all(object_list:list):
    for _, obj in object_list:
        obj.execute_properties()

pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
screen: pygame.Surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Entity 표시 예제")

# 블록 리스트 생성
block_list = []
block_width, block_height = 50, 50
for x in range(0, WINDOW_WIDTH, block_width):
    block = Block(x=x, y=WINDOW_HEIGHT - block_height, width=block_width, height=block_height)
    heapq.heappush(block_list, (DrawOrder.ENTITY.value, block))

# 엔티티 생성 (asset_path를 None으로 하면 사각형, 이미지 경로를 넣으면 이미지)
player: Player = Player(
    x=100, y=100, width=50, height=50,
    asset_path='assets/_Crouch.png'
)

player.add_property(Moveable(player.position, block_list))  # Player 객체에 Moveable 속성 추가
player.add_property(Fallable(player.position))  # Player 객체에 Fallable 속성 추가


object_list = []
heapq.heappush(object_list, (DrawOrder.ENTITY.value, player))
for _, block in block_list:
    heapq.heappush(object_list, (DrawOrder.ENTITY.value, block))

background_tile = pygame.image.load('assets/Background_Gray.png').convert()


clock: pygame.time.Clock = pygame.time.Clock()
running: bool = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.walk_left()
    if keys[pygame.K_RIGHT]:
        player.walk_right()


    # 객체 업데이트
    update_all(object_list)
    draw_all(screen, object_list, background_tile)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()


