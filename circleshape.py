from typing import ClassVar

import pygame


# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    # Subclasses can set this from main, e.g. Player.containers = (updatable, drawable)
    containers: ClassVar[tuple[pygame.sprite.AbstractGroup, ...]]

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
