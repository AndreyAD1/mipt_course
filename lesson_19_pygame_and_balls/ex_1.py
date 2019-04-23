import sys
import pygame


def get_new_velocity(init_x_velocity, init_y_velocity):
    friction_coefficient = 0.01

    result_x_velocity = init_x_velocity
    result_y_velocity = init_y_velocity

    if pygame.key.get_pressed()[pygame.K_UP]:
        result_y_velocity -= 5
    elif pygame.key.get_pressed()[pygame.K_DOWN]:
        result_y_velocity += 5
    elif pygame.key.get_pressed()[pygame.K_RIGHT]:
        result_x_velocity += 5
    elif pygame.key.get_pressed()[pygame.K_LEFT]:
        result_x_velocity -= 5
    else:
        pass

    result_x_velocity -= friction_coefficient * result_x_velocity
    result_y_velocity -= friction_coefficient * result_y_velocity

    return result_x_velocity, result_y_velocity


def start_ball_game(
        display_width=500,
        display_height=500,
        display_name='Balls',
        ball_radius=20,
        x_coord=30,
        y_coord=30,
        vx=50,
        vy=50,
):
    screen = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption(display_name)
    clock = pygame.time.Clock()

    while True:
        dt = clock.tick(50) / 1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        vx, vy = get_new_velocity(vx, vy)

        x_coord += vx * dt
        y_coord += vy * dt

        border_reached = any(
            [
                x_coord < ball_radius,
                x_coord > display_width - ball_radius,
                y_coord < ball_radius,
                y_coord > display_height - ball_radius
            ]
        )
        if border_reached:
            vx = -vx
            vy = -vy

        screen.fill((0, 0, 0))
        pygame.draw.circle(
            screen,
            (150, 10, 50),
            (int(x_coord), int(y_coord)),
            20
        )

        pygame.display.flip()


if __name__ == '__main__':
    start_ball_game()
