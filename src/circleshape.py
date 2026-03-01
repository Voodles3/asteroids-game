from abc import ABC, abstractmethod
from typing import Any, ClassVar

import pygame


# Base class for game objects
class CircleShape(pygame.sprite.Sprite, ABC):
    containers: ClassVar[tuple[pygame.sprite.Group[Any], ...]]

    def __init__(self, position: pygame.Vector2, radius: float) -> None:
        groups = getattr(self.__class__, "containers", ())
        super().__init__(*groups)

        self.position: pygame.Vector2 = position
        self.velocity: pygame.Vector2 = pygame.Vector2(0, 0)
        self.radius: float = radius

    @abstractmethod
    def draw(self, screen: pygame.Surface) -> None:
        pass

    @abstractmethod
    def update(self, dt: float) -> None:
        pass

    def collides_with(self, other: CircleShape) -> bool:
        if self.position.distance_to(other.position) < (self.radius + other.radius):
            return True
        return False
