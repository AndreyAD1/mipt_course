#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_21():
    look_around_functions = {
        wall_is_above: move_up,
        wall_is_beneath: move_down,
        wall_is_on_the_right: move_right,
        wall_is_on_the_left: move_left
    }
    opposite_directions = {
        wall_is_above: wall_is_beneath,
        wall_is_beneath: wall_is_above,
        wall_is_on_the_right: wall_is_on_the_left,
        wall_is_on_the_left: wall_is_on_the_right
    }
    for side in range(2):
        for direction in look_around_functions:
            if not direction():
                opposite_direction = opposite_directions[direction]
                look_around_functions.pop(opposite_direction)
                while not direction():
                    look_around_functions[direction]()
                break


if __name__ == '__main__':
    run_tasks()
