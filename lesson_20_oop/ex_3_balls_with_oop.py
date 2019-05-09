from itertools import combinations
from math import sqrt
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
        return Vector(self.x * multiplier.x, self.y * multiplier.y)

    def __rmul__(self, multiplier: float or int):
        return Vector(self.x * multiplier, self.y * multiplier)

    def __truediv__(self, divisor: float or int):
        return Vector(self.x / divisor, self.y / divisor)

    def __pow__(self, power, modulo=None):
        return Vector(self.x ** power, self.y ** power)

    @property
    def length(self):
        return sqrt(self.x**2 + self.y**2)

    @property
    def unit_vector(self):
        return Vector(self.x / self.length, self.y / self.length)

    def get_int_coords(self):
        return int(self.x), int(self.y)


class Ball:
    def __init__(self, coordinates: Vector):
        self.coords = coordinates
        self.color = (150, 10, 50)
        self.radius = 20
        self.velocity = Vector(0, 0)
        self.possible_colors = [(150, 10, 50), (50, 100, 150)]
        self.manual_control = False
        self.mass = 1
        self.collided_ball = None

    def refresh_coordinates(self, dt: float):
        self.coords += dt * self.velocity

    def accelerate(self, acceleration: Vector):
        self.velocity += acceleration

    def slow_down(self, friction_coefficient):
        self.velocity -= friction_coefficient * self.velocity

    def change_direction_after_wall_collision(self, x_border, y_border):
        if x_border:
            self.velocity.x = -self.velocity.x
        if y_border:
            self.velocity.y = -self.velocity.y

    def change_direction_after_ball_collision(self, ball_2):
        # ball_2 = self.collided_ball
        collision_unit_vector = (self.coords - ball_2.coords).unit_vector
        mass_sum = self.mass + ball_2.mass
        add_1 = -2 * ball_2.mass / mass_sum * self.momentum
        add_2 = 2 * self.mass / mass_sum * ball_2.momentum
        new_momentum = (add_1 + add_2) * collision_unit_vector ** 2
        self.velocity = new_momentum / self.mass
        self.collided_ball = None

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

    @property
    def momentum(self):
        return self.mass * self.velocity

    def click_is_on_the_ball(self, click_coords: Tuple[int]):
        hit_by_x = self.left_edge < click_coords[0] < self.right_edge
        hit_by_y = self.upper_edge < click_coords[1] < self.lower_edge
        return hit_by_x and hit_by_y

    def click_near_the_ball(self, click_coords: Tuple[int]):
        left_blind_space = self.left_edge - self.radius
        right_blind_space = self.right_edge + self.radius
        upper_blind_space = self.upper_edge - self.radius
        lower_blind_space = self.lower_edge + self.radius
        hit_by_x = left_blind_space < click_coords[0] < right_blind_space
        hit_by_y = upper_blind_space < click_coords[1] < lower_blind_space
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
        friction_coefficient=0.01
):
    screen = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption(display_name)
    clock = pygame.time.Clock()

    while True:
        click_position = ()
        click_on_blank_space = True
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

        if not balls:
            if click_position:
                x_coord, y_coord = click_position
                balls = [Ball(Vector(x_coord, y_coord))]
            continue

        # for ball_1, ball_2 in combinations(balls, 2):
        #     distance_between_balls = (ball_1.coords - ball_2.coords).length
        #     if distance_between_balls <= ball_1.radius + ball_2.radius:
        #         ball_1.collided_ball = ball_2
        #         ball_2.collided_ball = ball_1

        for ball in balls:
            if click_position:
                if ball.click_near_the_ball(click_position):
                    click_on_blank_space = False
                if ball.click_is_on_the_ball(click_position):
                    ball.change_color()
                    ball.switch_manual_control()

            ball.refresh_coordinates(dt)
            x_border_reached = (
                    ball.left_edge < 0 or ball.right_edge > display_width
            )
            y_border_reached = (
                    ball.upper_edge < 0 or ball.lower_edge > display_height
            )
            ball.change_direction_after_wall_collision(
                x_border_reached,
                y_border_reached
            )

            # if ball.collided_ball:
            #     ball.change_direction_after_ball_collision()

            if ball.manual_control:
                ball.accelerate(acceleration)

            ball.slow_down(friction_coefficient)

        for ball_1, ball_2 in combinations(balls, 2):
            distance_between_balls = (ball_1.coords - ball_2.coords).length
            if distance_between_balls <= ball_1.radius + ball_2.radius:
                ball_1.change_direction_after_ball_collision(ball_2)
                ball_2.change_direction_after_ball_collision(ball_1)

        if click_position and click_on_blank_space:
            x_coord, y_coord = click_position
            balls.append(Ball(Vector(x_coord, y_coord)))

        screen.fill((0, 0, 0))
        [ball.render(screen) for ball in balls]
        pygame.display.flip()


if __name__ == '__main__':
    # start_game(balls=[Ball(Vector(200, 100)), Ball(Vector(250, 300))])
    start_game()
