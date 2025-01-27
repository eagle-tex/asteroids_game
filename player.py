import pygame
from pygame.sprite import Sprite, Group
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_SPEED, PLAYER_TURN_SPEED


class Player(CircleShape, Sprite):
    containers: tuple[Group, Group] = (Group(), Group())

    def __init__(self, x: int, y: int) -> None:
        CircleShape.__init__(self, x, y, PLAYER_RADIUS)
        assert self.containers is not None
        Sprite.__init__(self, *Player.containers)
        self.position: pygame.Vector2 = pygame.Vector2(x, y)
        self.rotation: int = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt, direction: int):
        self.rotation += direction * PLAYER_TURN_SPEED * dt

    def update(self, dt: float):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_q]:
            self.rotate(dt, -1)  # turn left

        if keys[pygame.K_d]:
            self.rotate(dt, 1)  # turn right

        if keys[pygame.K_z]:
            self.move(dt, 1)

        if keys[pygame.K_s]:
            self.move(dt, -1)

    def move(self, dt: float, direction):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * direction * PLAYER_SPEED * dt
