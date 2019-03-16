import graphics as gr
import copy
from math import sqrt

SIZE_X = 400
SIZE_Y = 400
BALL_RADIUS = 10
GRAVITATIONAL_CONSTANT = 20
GRAVITY_CENTER = gr.Point(200, 200)
window = gr.GraphWin('Solar system', SIZE_X, SIZE_Y)


def get_new_point(point_1, point_2):
    new_point = gr.Point(point_1.x + point_2.x, point_1.y + point_2.y)
    return new_point


def draw_ball(coordinates):
    circle = gr.Circle(coordinates, BALL_RADIUS)
    circle.setFill('red')
    circle.draw(window)


def clear_window():
    rectangle = gr.Rectangle(gr.Point(0, 0), gr.Point(SIZE_X, SIZE_Y))
    rectangle.setFill('green')
    rectangle.draw(window)


def get_speed_vector_after_reflection(coordinates, speed):
    point_speed = copy.deepcopy(speed)
    if coordinates.x < 0 or coordinates.x > SIZE_X:
        point_speed.x = -point_speed.x
    if coordinates.y < 0 or coordinates.y > SIZE_Y:
        point_speed.y = -point_speed.y
    return point_speed


def get_acceleration(position):
    x_difference = (position.x - GRAVITY_CENTER.x)
    y_difference = (position.y - GRAVITY_CENTER.y)
    distance_from_center = sqrt(x_difference ** 2 + y_difference ** 2)
    x_acceleration = -x_difference * GRAVITATIONAL_CONSTANT/distance_from_center
    y_acceleration = -y_difference * GRAVITATIONAL_CONSTANT/ distance_from_center
    acceleration = gr.Point(x_acceleration, y_acceleration)
    return acceleration


position = gr.Point(150, 200)
velocity = gr.Point(0, 0)
circle = gr.Circle(position, BALL_RADIUS)
circle.draw(window)


for _ in range(10000):
    clear_window()
    # draw_ball(position)
    position = get_new_point(position, velocity)

    acceleration = get_acceleration(position)
    velocity = get_new_point(velocity, acceleration)
    velocity = get_speed_vector_after_reflection(position, velocity)
    gr.time.sleep(0.02)

window.getMouse()
window.close()
