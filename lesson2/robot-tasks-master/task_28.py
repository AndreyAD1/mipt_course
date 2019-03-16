#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_6():
    filled_cells_number = 0
    while True:
        if cell_is_filled():
            filled_cells_number += 1
        if filled_cells_number == 5:
            break
        move_right()


if __name__ == '__main__':
    run_tasks()
