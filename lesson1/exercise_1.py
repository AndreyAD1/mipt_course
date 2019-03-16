import turtle
import math


my_turtle = turtle.Turtle()
my_turtle.shape('turtle')
# spiral_step = 10
# for angle_degrees in range(5000):
#     angle_radians = math.radians(angle_degrees)
#     radius = spiral_step * angle_radians
#     x_coord = radius * math.cos(angle_radians)
#     y_coord = radius * math.sin(angle_radians)
#     my_turtle.setheading(angle_degrees+90)
#     my_turtle.setposition(x_coord, y_coord)
side_number = 30
side_length = 10
side_step = 10
for side in range(side_number):
    my_turtle.forward(side_length)
    my_turtle.left(90)
    side_length += side_step
turtle.done()
