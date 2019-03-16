#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_9_3():
    side_length = 1
    while not wall_is_on_the_right():
        move_right()
        side_length += 1

    for row in range(side_length):
        while not wall_is_on_the_left():
            move_left()
        row_number = row + 1
        for column in range(side_length):
            column_number = column + 1
            if column_number != row_number and column_number != side_length - row_number + 1:
                fill_cell()
            if not wall_is_on_the_right():
                move_right()
        if not wall_is_beneath():
            move_down()
    while not wall_is_on_the_left():
        move_left()


if __name__ == '__main__':
    run_tasks()
