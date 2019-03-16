import turtle


def draw(l, n):
    if n == 0:
        turtle.left(180)
        return

    x = l / (n + 1)
    for i in range(n):
        turtle.forward(x)
        turtle.left(45)
        draw(0.5 * x * (n - i - 1), n - i - 1)
        turtle.left(90)
        draw(0.5 * x * (n - i - 1), n - i - 1)
        turtle.right(135)

    turtle.forward(x)
    turtle.left(180)
    turtle.forward(l)


def draw_koch_curve(side_length, recursion_depth):
    side_length = side_length / 3
    if recursion_depth == 1:
        turtle.forward(side_length)
        turtle.left(60)
        turtle.forward(side_length)
        turtle.right(120)
        turtle.forward(side_length)
        turtle.left(60)
        turtle.forward(side_length)
        return
    draw_koch_curve(side_length, recursion_depth - 1)
    turtle.left(60)
    draw_koch_curve(side_length, recursion_depth - 1)
    turtle.right(120)
    draw_koch_curve(side_length, recursion_depth - 1)
    turtle.left(60)
    draw_koch_curve(side_length, recursion_depth - 1)


def draw_koch_snowflake(side_length, recursion_depth):
    for side in range(3):
        draw_koch_curve(side_length, recursion_depth)
        turtle.right(120)


# draw(400, 2)
turtle.speed('fastest')
turtle.penup()
turtle.goto(-300, 200)
turtle.pendown()
# draw_koch_curve(600, 6)
draw_koch_snowflake(600, 5)
turtle.done()
