import graphics as gr

SIZE_X = 800
SIZE_Y = 800

window = gr.GraphWin("Model", SIZE_X, SIZE_Y)

thread_length = 50
pendulum_basis = gr.Point(400, 400)
balance_point = gr.Point(pendulum_basis.x, pendulum_basis.y - thread_length)

coords = gr.Point(350, 350)
velocity = gr.Point(0, 0)
acceleration = gr.Point(0, 0)


def add(point_1, point_2):
    new_point = gr.Point(point_1.x + point_2.x,
                         point_1.y + point_2.y)

    return new_point


def sub (point_1, point_2):
    new_point = gr.Point(point_1.x - point_2.x,
                         point_1.y - point_2.y)

    return new_point


def clear_window():
    rectangle = gr.Rectangle(gr.Point(0, 0), gr.Point(SIZE_X, SIZE_Y))
    rectangle.setFill('green')
    rectangle.draw(window)

    sun = gr.Circle(gr.Point(400, 400), 50)
    sun.setFill('yellow')
    sun.draw(window)


def draw_ball(coords):
    circle = gr.Circle(coords, 10)
    circle.setFill('red')

    circle.draw(window)


def check_coords(coords, velocity):
    if coords.x < 0 or coords.x > SIZE_X:
        velocity.x = -velocity.x

    if coords.y < 0 or coords.y > SIZE_Y:
        velocity.y = -velocity.y


def update_coords(coords, velocity):
    return add(coords, velocity)


def update_velocity(velocity, acceleration):
    return add(velocity, acceleration)


def update_acceleration(ball_coords, center_coords):
    diff = sub(ball_coords, center_coords)
    distance_2 = (diff.x ** 2 + diff.y ** 2) ** 0.5
    G = 10
    acceleration = -G * distance_2 / thread_length
    acceleration_x = acceleration * distance_2 / thread_length
    acceleration_y = (acceleration ** 2 - acceleration_x ** 2) ** (1/2)

    return gr.Point(acceleration_x, acceleration_y)


clear_window()
circle = gr.Circle(coords, 10)

# circle.draw(window)

while True:
    acceleration = update_acceleration(coords, balance_point)
    velocity = update_velocity(velocity, acceleration)
    circle.move(velocity.x, velocity.y)
    coords = update_coords(coords, velocity)


    gr.time.sleep(0.02)
