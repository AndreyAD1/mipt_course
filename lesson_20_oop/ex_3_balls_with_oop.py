from typing import List, Tuple
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

    def __sub__(self, subtrahend):
        return Vector(self.x - subtrahend.x, self.y - subtrahend.y)

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
        self.possible_colors = [(150, 10, 50), (50, 100, 150)]
        self.friction_coefficient = 0.01
        self.manual_control = False

    def refresh_coordinates(self, dt: float):
        self.coords += self.velocity * dt

    def refresh_velocity(self, acceleration: Vector):
        self.velocity += acceleration
        self.velocity -= self.velocity * self.friction_coefficient

    def change_direction_after_collision(self, x_border, y_border):
        if x_border:
            self.velocity.x = -self.velocity.x
        if y_border:
            self.velocity.y = -self.velocity.y

    def render(self, canvas):
        pygame.draw.circle(
            canvas,
            self.color,
            self.coords.get_int_coords(),
            self.radius
        )

    def switch_manual_control(self):
        self.manual_control = not self.manual_control

    @property
    def x(self):
        return self.coords.x

    @property
    def y(self):
        return self.coords.y

    @property
    def left_edge(self):
        return self.x - self.radius

    @property
    def right_edge(self):
        return self.x + self.radius

    @property
    def upper_edge(self):
        return self.y - self.radius

    @property
    def lower_edge(self):
        return self.y + self.radius

    def click_is_on_the_ball(self, click_coords: Tuple[int]):
        hit_by_x = self.left_edge < click_coords[0] < self.right_edge
        hit_by_y = self.upper_edge < click_coords[1] < self.lower_edge
        return hit_by_x and hit_by_y

    def change_color(self):
        initial_color = self.color
        self.possible_colors.remove(self.color)
        self.color = self.possible_colors[0]
        self.possible_colors.append(initial_color)


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
        click_position = ()
        x_acceleration = 0
        y_acceleration = 0

        dt = clock.tick(50) / 1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                click_position = event.pos

        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            x_acceleration += 5
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            x_acceleration -= 5
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            y_acceleration += 5
        if pygame.key.get_pressed()[pygame.K_UP]:
            y_acceleration -= 5

        acceleration = Vector(x_acceleration, y_acceleration)

        for ball in balls:
            ball.refresh_coordinates(dt)
            x_border_reached = (
                    ball.left_edge < 0 or ball.right_edge > display_width
            )
            y_border_reached = (
                    ball.upper_edge < 0 or ball.lower_edge > display_height
            )
            ball.change_direction_after_collision(
                x_border_reached,
                y_border_reached
            )
            if click_position and ball.click_is_on_the_ball(click_position):
                ball.change_color()
                ball.switch_manual_control()

            if ball.manual_control:
                ball.refresh_velocity(acceleration)

        screen.fill((0, 0, 0))

        [ball.render(screen) for ball in balls]

        pygame.display.flip()


if __name__ == '__main__':
    start_game(balls=[Ball(Vector(200, 100)), Ball(Vector(250, 300))])
