import pygame
from pygame.sprite import Group, Sprite
from circleshape import CircleShape
from constants import SHOT_RADIUS


class Shot(CircleShape, Sprite):
    shots_containers: tuple[Group, ...] | None = None

    def __init__(self, x, y, radius):
        CircleShape.__init__(self, x, y, radius)
        assert Shot.shots_containers is not None  # Assert before using
        Sprite.__init__(self, *Shot.shots_containers)

    def draw(self, screen):
        pygame.draw.circle(screen, "green", self.position, self.radius)

    def update(self, dt: float):
        self.position += self.velocity * dt
