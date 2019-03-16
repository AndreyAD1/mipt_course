import turtle


def draw_dragon_curve_left(recursion_depth, side_length):
    if recursion_depth == 0:
        turtle.forward(side_length)
        return

    draw_dragon_curve_left(recursion_depth - 1, side_length / (2 ** 0.5))
    turtle.right(90)
    draw_dragon_curve_right(recursion_depth - 1, side_length / (2 ** 0.5))


def draw_dragon_curve_right(recursion_depth, side_length):
    if recursion_depth == 0:
        turtle.forward(side_length)
        return

    turtle.right(45)
    draw_dragon_curve_right(recursion_depth - 1, side_length / (2 ** 0.5))
    turtle.left(90)
    draw_dragon_curve_left(recursion_depth - 1, side_length / (2 ** 0.5))


if __name__ == '__main__':
    turtle.speed('slowest')
    turtle.penup()
    turtle.goto(-250, 0)
    turtle.pendown()
    draw_dragon_curve_right(3, 200)
    turtle.done()
