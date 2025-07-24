from objects.properties.prime_property  import PrimeProperty
from objects.entity import Entity
import pygame

PERIORITY = -1

class Moveable(PrimeProperty):
    def __init__(self, position:dict[str:float], block_list:list) -> None:
        """
        Initialize the Moveable property with a given priority.

        :param priority: The priority of the Moveable property.
        """
        super().__init__(PERIORITY)
        self.position: dict[str: float] = position
        self.block_list = block_list

    def execute(self) -> None:
        """
        Update the position based on the current velocity.
        """
        
        # 가상 이동 후 충돌 체크
        self.position['x'] += self.position['dx']
        for _, block in self.block_list:
            if self.is_colliding(block):
                self.position['x'] -= self.position['dx'] # 충돌 시 x 이동 취소
                break
        
        self.position['y'] += self.position['dy']
        for _, block in self.block_list:
            if self.is_colliding(block):
                self.position['y'] -= self.position['dy'] # 충돌 시 y 이동 취소
                break

        self.position['dx'] = 0
        self.position['dy'] = 0

    def move(self, dx: float, dy: float) -> None:
        """
        Set the velocity of the object.

        :param dx: The change in x-coordinate.
        :param dy: The change in y-coordinate.
        """
        self.position['dx'] = dx
        self.position['dy'] = dy

    def is_colliding(self, other: Entity) -> bool:
        self_rect = pygame.Rect(self.position['x'], self.position['y'], self.position['width'], self.position['height'])
        other_rect = pygame.Rect(other.position['x'], other.position['y'], other.width, other.height)
        return self_rect.colliderect(other_rect)
