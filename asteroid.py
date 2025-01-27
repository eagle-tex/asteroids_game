import pygame
from pygame.sprite import Group, Sprite
from circleshape import CircleShape


class Asteroid(CircleShape, Sprite):
    containers: tuple[Group, Group, Group] | None = None

    def __init__(self, x, y, radius):
        CircleShape.__init__(self, x, y, radius)
        assert Asteroid.containers is not None  # Assert before using
        Sprite.__init__(self, *Asteroid.containers)

    def draw(self, screen):
        pygame.draw.circle(screen, "red", self.position, self.radius, width=2)

    def update(self, dt: float):
        self.position += self.velocity * dt
