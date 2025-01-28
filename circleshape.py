import pygame
from pygame.sprite import Group


# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    containers: tuple = ()  # Type hint for containers

    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(*self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius: float = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def collides(self, other: "CircleShape") -> bool:
        distance_between = self.position.distance_to(other.position)
        # pygame.Vector2.distance_to(self.position, other.position)
        if distance_between > self.radius + other.radius:
            return False
        return True
