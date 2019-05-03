from typing import List
import sys

import pygame


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return 'Vector x={}, y ={}'.format(self.x, self.y)

    def __add__(self, addend):
        new_x = self.x + addend.x
        new_y = self.y + addend.y
        return Vector(new_x, new_y)

    def __mul__(self, multiplier):
        return Vector(self.x * multiplier, self.y * multiplier)

    def get_int_coords(self):
        return int(self.x), int(self.y)


class Ball:
    def __init__(self, coordinates: Vector):
        self.coords = coordinates
        self.color = (150, 10, 50)
        self.radius = 20
        self.velocity = Vector(50, 50)

    def get_new_coordinates(self, dt: float):
        self.coords += self.velocity * dt

    def change_direction_if_reach_a_wall(self, max_x: int, max_y: int):
        x_border_reached = (
                self.coords.x < self.radius or
                self.coords.x > max_x - self.radius
        )
        y_border_reached = (
                self.coords.y < self.radius or
                self.coords.y > max_y - self.radius
        )
        if x_border_reached:
            self.velocity.x = -self.velocity.x
        if y_border_reached:
            self.velocity.y = -self.velocity.y

    def render(self, canvas):
        pygame.draw.circle(
            canvas,
            self.color,
            self.coords.get_int_coords(),
            self.radius
        )


def start_game(
        balls: List[Ball] = None,
        display_width=500,
        display_height=500,
        display_name='Balls',
):
    screen = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption(display_name)
    clock = pygame.time.Clock()

    while True:
        dt = clock.tick(50) / 1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        for ball in balls:
            ball.get_new_coordinates(dt)
            ball.change_direction_if_reach_a_wall(display_width, display_height)

        screen.fill((0, 0, 0))

        [ball.render(screen) for ball in balls]

        pygame.display.flip()


if __name__ == '__main__':
    start_game(balls=[Ball(Vector(200, 100)), Ball(Vector(250, 300))])
