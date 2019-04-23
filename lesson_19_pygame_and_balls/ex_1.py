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


def check_collisions():
    pass


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
            new_ball_features[ball_id] = {
                'coords': [new_vx * dt, new_vy * dt],
                'velocity': [new_vx, new_vy]
            }

        balls = new_ball_features

        check_collisions()
        # border_reached = any(
        #     [
        #         x_coord < ball_radius,
        #         x_coord > display_width - ball_radius,
        #         y_coord < ball_radius,
        #         y_coord > display_height - ball_radius
        #     ]
        # )
        # if border_reached:
        #     vx = -vx
        #     vy = -vy

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
    start_ball_game({'ball_1': {'coords': [30, 30], 'velocity': [50, 50]}})
