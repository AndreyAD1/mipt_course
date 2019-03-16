import turtle


def draw_minkowski_sausage(side_length, recursion_depth):
    if recursion_depth == 0:
        turtle.forward(side_length)
        return

    draw_minkowski_sausage(side_length / 4, recursion_depth - 1)
    turtle.left(90)
    draw_minkowski_sausage(side_length / 4, recursion_depth - 1)
    turtle.right(90)
    draw_minkowski_sausage(side_length / 4, recursion_depth - 1)
    turtle.right(90)
    draw_minkowski_sausage(side_length / 4, recursion_depth - 1)
    draw_minkowski_sausage(side_length / 4, recursion_depth - 1)
    turtle.left(90)
    draw_minkowski_sausage(side_length / 4, recursion_depth - 1)
    turtle.left(90)
    draw_minkowski_sausage(side_length / 4, recursion_depth - 1)
    turtle.right(90)
    draw_minkowski_sausage(side_length / 4, recursion_depth - 1)


if __name__ == '__main__':
    turtle.speed('fastest')
    turtle.penup()
    turtle.goto(-300, 0)
    turtle.pendown()
    draw_minkowski_sausage(500, 3)
    turtle.done()
