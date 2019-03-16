import turtle


my_turtle = turtle.Turtle()
my_turtle.shape('turtle')
petal_pair_number = 3
big_radius = 20
small_radius = 5
my_turtle.left(90)

for petal_pair in range(petal_pair_number):
    my_turtle.circle(-big_radius, extent=180)
    my_turtle.circle(-small_radius, extent=180)

turtle.done()