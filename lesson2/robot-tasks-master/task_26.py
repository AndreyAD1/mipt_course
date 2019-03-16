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


def draw_cross_line(line_length):
    for cross_num, cross in enumerate(range(line_length)):
        draw_a_cross()
        if cross_num < line_length - 1:
            move_right(4)


@task(delay=0.02)
def task_2_4():
    line_number = 5
    crosses_in_a_line = 10
    for line_num, cross_line in enumerate(range(line_number)):
        draw_cross_line(crosses_in_a_line)
        while not wall_is_on_the_left():
            move_left()
        if line_num < line_number - 1:
            move_down(4)


if __name__ == '__main__':
    run_tasks()
