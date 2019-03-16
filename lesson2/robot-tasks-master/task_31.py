#!/usr/bin/python3

from pyrob.api import *


def descend_to_next_level():
    while not wall_is_beneath():
        move_down()
    return


def pass_a_level():
    is_lowest_level = False
    while not wall_is_on_the_right():
        if not wall_is_beneath():
            return is_lowest_level
        move_right()
    while not wall_is_on_the_left():
        if not wall_is_beneath():
            return is_lowest_level
        move_left()
    is_lowest_level = True
    return is_lowest_level


@task(delay=0.05)
def task_8_30():
    while True:
        descend_to_next_level()
        lowest_level = pass_a_level()
        if lowest_level:
            break


if __name__ == '__main__':
    run_tasks()
