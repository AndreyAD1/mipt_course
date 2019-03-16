#!/usr/bin/python3

from pyrob.api import *
from copy import copy


def pass_passage(cells_count):
    cells_count_copy = copy(cells_count)
    while not wall_is_above():
        move_up()
        if cell_is_filled():
            cells_count_copy += 1
        fill_cell()
    while not wall_is_beneath():
        move_down()
    return cells_count_copy


@task(delay=0.07)
def task_8_18():
    number_of_preliminary_filled_cells = 0
    while not wall_is_on_the_right():
        if not wall_is_above():
            number_of_preliminary_filled_cells = pass_passage(
                number_of_preliminary_filled_cells
            )
        if wall_is_above():
            fill_cell()
        move_right()
    mov('ax', number_of_preliminary_filled_cells)


if __name__ == '__main__':
    run_tasks()
