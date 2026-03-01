from typing import ClassVar

import pygame


# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    containers: ClassVar[tuple]

    def __init__(self, x, y, radius):
        groups = getattr(self.__class__, "containers", ())
        super().__init__(*groups)

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # must override
        pass

    def update(self, dt):
        # must override
        pass

    def collides_with(self, other: CircleShape) -> bool:
        if self.position.distance_to(other.position) < (self.radius + other.radius):
            return True
        return False
