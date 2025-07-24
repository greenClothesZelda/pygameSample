import pygame
from typing import Optional

from objects.prime.rectangle import Rectangle
from env import isDebug
from objects.properties.prime_property import PrimeProperty


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
        self.__properties: list = []
        if asset_path:
            self.image = pygame.image.load(asset_path)
            self.image = pygame.transform.scale(self.image, (int(width), int(height)))

    def draw(self, surface: pygame.Surface) -> None:
        if not isinstance(surface, pygame.Surface):
            raise TypeError(f"Expected a pygame.Surface, got {type(surface)}")

        if not self.is_active or not self.is_display:
            return
        if self.image:
            surface.blit(self.image, (int(self.position['x']), int(self.position['y'])))
        else:
            super().draw(surface)
        if isDebug:
            # 빨간색 테두리 그리기
            pygame.draw.rect(surface, (255, 0, 0), (int(self.position['x']), int(self.position['y']), int(self.width), int(self.height)), 2)


    def add_property(self, property) -> None:
        if not isinstance(property, PrimeProperty):
            raise TypeError(f"Expected a PrimeProperty, got {type(property)}")
        if property in self.__properties:
            raise ValueError(f"Property {property} already exists in {self}")
        self.__properties.append(property)

    def remove_property(self, property) -> None:
        if not isinstance(property, PrimeProperty):
            raise TypeError(f"Expected a PrimeProperty, got {type(property)}")
        if property not in self.__properties:
            raise ValueError(f"Property {property} does not exist in {self}")
        self.__properties.remove(property)

    def execute_properties(self) -> None:
        for property in self.__properties:
            property.execute()

