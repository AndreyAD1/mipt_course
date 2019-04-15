import sys
import pygame

width = 500
height = 500

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('YAHOOOO')
clock = pygame.time.Clock()

x = 30
y = 30
vx = 50
vy = 50
BALL_RADIUS = 20

while True:
    dt = clock.tick(50) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    if pygame.key.get_pressed()[pygame.K_UP]:
        vy -= 5
    elif pygame.key.get_pressed()[pygame.K_DOWN]:
        vy += 5
    elif pygame.key.get_pressed()[pygame.K_RIGHT]:
        vx += 5
    elif pygame.key.get_pressed()[pygame.K_LEFT]:
        vx -= 5
    else:
        pass

    vx -= 0.01 * vx
    vy -= 0.01 * vy

    x += vx * dt
    y += vy * dt

    border_reached = any(
        [
            x < BALL_RADIUS,
            x > width - BALL_RADIUS,
            y < BALL_RADIUS,
            y > height - BALL_RADIUS
        ]
    )
    if border_reached:
        vx = -vx
        vy = -vy

    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (150, 10, 50), (int(x), int(y)), 20)

    pygame.display.flip()
