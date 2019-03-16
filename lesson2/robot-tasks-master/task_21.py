#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_11():
    row_number = 13
    column_pairs = 7
    for num, column in enumerate(range(column_pairs)):
        move_right()
        for row in range(row_number):
            move_down()
            fill_cell()
        if num < len(range(column_pairs)) - 1:
            row_number -= 2
            move_right()
            fill_cell()
            for row in range(row_number):
                move_up()
                fill_cell()
    move_down()
    move_left(12)


if __name__ == '__main__':
    run_tasks()
