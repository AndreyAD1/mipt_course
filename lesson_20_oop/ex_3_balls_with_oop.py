from typing import List
import sys

import pygame


class Ball:
    def __init__(self, x_coord, y_coord):
        self.x = x_coord
        self.y = y_coord
        self.color = (150, 10 ,50)
        self.radius = 20


class Vector:
    pass


def start_game(
        balls: List[Ball] = None,
        display_width=500,
        display_height=500,
        display_name='Balls',
        ball_radius=20,
):
    screen = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption(display_name)
    clock = pygame.time.Clock()

    while True:
        dt = clock.tick(50) / 1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill((0, 0, 0))

        for ball in balls:
            pygame.draw.circle(
                screen,
                ball.color,
                (ball.x, ball.y),
                ball.radius
            )

        pygame.display.flip()


if __name__ == '__main__':
    start_game(balls=[Ball(100, 100), Ball(200, 200)])
