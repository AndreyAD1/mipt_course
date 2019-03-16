import turtle
from math import sin, radians


def draw_regular_polygon(side_number, circumscribed_circle_radius, drawer):
    angle_between_radiuses = sin(radians(360 / (2 * side_number)))
    side_length = circumscribed_circle_radius * 2 * angle_between_radiuses
    internal_angle = 180 * (side_number - 2) / side_number
    initial_drawer_direction = (360 - internal_angle) / 2
    drawer.left(initial_drawer_direction)
    for side in range(side_number):
        drawer.forward(side_length)
        drawer.left(180 - internal_angle)
    drawer.right(initial_drawer_direction)


my_turtle = turtle.Turtle()
my_turtle.shape('turtle')
polygon_number = 10
polygon_shift = 20
circumscribed_radius = 30

for side_quantity in range(3, polygon_number + 1, 1):
    my_turtle.pendown()
    draw_regular_polygon(side_quantity, circumscribed_radius, my_turtle)
    circumscribed_radius += polygon_shift
    my_turtle.penup()
    my_turtle.forward(polygon_shift)
turtle.done()
