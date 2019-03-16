#!/usr/bin/python3

from pyrob.api import *


def draw_a_cross():
    side_length = 3
    move_right()
    fill_cell()
    for step in range(side_length - 1):
        move_down()
        fill_cell()
    move_right()
    move_up()
    fill_cell()
    for step in range(side_length - 1):
        move_left()
        fill_cell()
    move_up()


@task
def task_2_1():
    move_down()
    move_right()
    draw_a_cross()


if __name__ == '__main__':
    run_tasks()
