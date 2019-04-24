from itertools import combinations
from math import hypot, atan, sin, cos, pi
import sys
from typing import List, Tuple, Dict

import pygame


def get_new_velocity(coordinates: List) -> Tuple:
    friction_coefficient = 0.01

    x_velocity, y_velocity = coordinates

    if pygame.key.get_pressed()[pygame.K_UP]:
        y_velocity -= 5
    elif pygame.key.get_pressed()[pygame.K_DOWN]:
        y_velocity += 5
    elif pygame.key.get_pressed()[pygame.K_RIGHT]:
        x_velocity += 5
    elif pygame.key.get_pressed()[pygame.K_LEFT]:
        x_velocity -= 5
    else:
        pass

    x_velocity -= friction_coefficient * x_velocity
    y_velocity -= friction_coefficient * y_velocity

    return x_velocity, y_velocity


def check_collisions(x_coord, y_coord, vx, vy, max_x, max_y, ball_radius):
    x_border_reached = x_coord < ball_radius or x_coord > max_x - ball_radius
    y_border_reached = y_coord < ball_radius or y_coord > max_y - ball_radius
    if x_border_reached:
        vx = -vx
    if y_border_reached:
        vy = -vy
    return vx, vy


def get_velocity_after_collision(velocity: tuple, angle) -> tuple:
    init_vx, init_vy = velocity
    init_v_along_collision = init_vx * cos(angle) + init_vy * cos(pi/2 - angle)
    init_v_across_collision = init_vy * sin(angle) + init_vx * sin(pi/2 - angle)
    result_v_along_collision = -init_v_along_collision
    result_v_across_collision = init_v_across_collision
    result_vx = result_v_along_collision * cos(angle) + result_v_across_collision * cos(pi/2 - angle)
    result_vy = result_v_along_collision * sin(angle) + result_v_across_collision * sin(pi/2 - angle)
    return result_vx, result_vy


def start_ball_game(
        balls: Dict[str, Dict[str, List]],
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

        new_ball_features = {}
        for ball_id, ball_features in balls.items():
            new_vx, new_vy = get_new_velocity(ball_features['velocity'])
            x_coord, y_coord = ball_features['coords']
            new_x_coord = x_coord + new_vx * dt
            new_y_coord = y_coord + new_vy * dt
            new_vx, new_vy = check_collisions(
                new_x_coord,
                new_y_coord,
                new_vx,
                new_vy,
                display_width,
                display_height,
                ball_radius
            )
            new_ball_features[ball_id] = {
                'coords': [x_coord + new_vx * dt, y_coord + new_vy * dt],
                'velocity': [new_vx, new_vy]
            }

        balls = new_ball_features

        collided_balls = []
        for first_ball_id, second_ball_id in combinations(balls, 2):
            x1, y1 = balls[first_ball_id]['coords']
            x2, y2 = balls[second_ball_id]['coords']
            distance_between_ball_centres = hypot(x2 - x1, y2 - y1)
            if distance_between_ball_centres < ball_radius * 2:
                collided_balls.append((first_ball_id, second_ball_id))

        for first_ball_id, second_ball_id in collided_balls:
            x1, y1 = balls[first_ball_id]['coords']
            x2, y2 = balls[second_ball_id]['coords']
            collision_angle = atan(y2 - y1 / x2 - x1)
            first_ball_velocity = balls[first_ball_id]['velocity']
            balls[first_ball_id]['velocity'] = get_velocity_after_collision(
                first_ball_velocity,
                collision_angle
            )
            second_ball_velocity = balls[second_ball_id]['velocity']
            balls[second_ball_id]['velocity'] = get_velocity_after_collision(
                second_ball_velocity,
                collision_angle
            )

        screen.fill((0, 0, 0))
        for ball_features in balls.values():
            pygame.draw.circle(
                screen,
                (150, 10, 50),
                (
                    int(ball_features['coords'][0]),
                    int(ball_features['coords'][1])
                ),
                ball_radius
            )

        pygame.display.flip()


if __name__ == '__main__':
    start_ball_game(
        {
            'ball_1': {'coords': [30, 30], 'velocity': [50, 50]},
            'ball_2': {'coords': [120, 120], 'velocity': [-50, -50]}
        },
    )
