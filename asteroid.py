import random
from typing import Any
import pygame
from pygame.sprite import Sprite
from circleshape import CircleShape
from constants import (
    ASTEROID_MIN_RADIUS,
    ASTEROID_SPLIT_RANDOM_ANGLE_MAX,
    ASTEROID_SPLIT_RANDOM_ANGLE_MIN,
    ASTEROID_SPLIT_SPEED_FACTOR,
)


class Asteroid(CircleShape, Sprite):
    # containers: tuple[Group, Group] | None = None
    asteroids_containers: tuple[Any, ...] | None = None

    def __init__(self, x, y, radius):
        CircleShape.__init__(self, x, y, radius)
        assert Asteroid.asteroids_containers is not None  # Assert before using
        Sprite.__init__(self, *Asteroid.asteroids_containers)

    def draw(self, screen):
        pygame.draw.circle(screen, "red", self.position, self.radius, width=2)

    def update(self, dt: float):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        random_angle = random.uniform(
            ASTEROID_SPLIT_RANDOM_ANGLE_MIN, ASTEROID_SPLIT_RANDOM_ANGLE_MAX
        )
        vector1 = self.velocity.rotate(random_angle)
        vector2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = vector1 * ASTEROID_SPLIT_SPEED_FACTOR

        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = vector2 * ASTEROID_SPLIT_SPEED_FACTOR
