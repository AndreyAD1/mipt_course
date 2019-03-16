#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_4():
    while not wall_is_beneath():
        move_down()
    wall_length = 0
    while wall_is_beneath():
        wall_length += 1
        move_right()
    move_down()
    move_left(wall_length)


if __name__ == '__main__':
    run_tasks()
