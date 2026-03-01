import random

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, position: pygame.Vector2, radius: float) -> None:
        super().__init__(position, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self) -> None:
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split)")
        # Determine new random angle, directions, and radius
        angle = random.uniform(20, 50)
        new_direction_1 = self.velocity.rotate(angle)
        new_direction_2 = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # Instantiate both new asteroids
        asteroid_1 = Asteroid(self.position, new_radius)
        asteroid_2 = Asteroid(self.position, new_radius)

        # Set the new asteroids' velocity
        asteroid_1.velocity = new_direction_1 * 1.2
        asteroid_2.velocity = new_direction_2 * 1.2
