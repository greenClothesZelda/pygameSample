from objects.entity import Entity
from typing import Optional
import pygame

class Block(Entity):
    def __init__(self, x: float, y: float, width: float, height: float, asset_path: Optional[str] = None) -> None:
        super().__init__(x, y, width, height, color=(100, 100, 100), asset_path=asset_path)
