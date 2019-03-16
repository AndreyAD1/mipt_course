import turtle


def draw_levi_c_curve(recursion_depth, side_length):
    assert recursion_depth >= 0
    if recursion_depth == 0:
        turtle.forward(side_length)
        return

    turtle.left(45)
    draw_levi_c_curve(recursion_depth - 1, side_length / (2 ** 0.5))
    turtle.right(90)
    draw_levi_c_curve(recursion_depth - 1, side_length / (2 ** 0.5))
    turtle.left(45)


if __name__ == '__main__':
    turtle.speed('fastest')
    turtle.penup()
    turtle.goto(-250, 0)
    turtle.pendown()
    draw_levi_c_curve(11, 400)
    turtle.done()
