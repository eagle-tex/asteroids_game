#!./venv/bin/python3.13

# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player


def main():
    pygame.init()

    clock = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    # variable not used but player creation is necessary
    initial_player = Player(int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # pause the game for 1/60th of a second
        dt = clock.tick(60) / 1000

        # update all game objects
        for obj in updatable:
            obj.update(dt)

        # clear the screen
        pygame.Surface.fill(screen, "black")

        # draw game objects
        for obj in drawable:
            obj.draw(screen)

        # show the frame
        pygame.display.flip()


if __name__ == "__main__":
    main()
