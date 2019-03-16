#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_5():
    gap = 1
    move_right()
    while not wall_is_on_the_right():
        fill_cell()
        for _ in range(gap):
            move_right()
            if wall_is_on_the_right():
                print('meet wall')
                break
        gap += 1


if __name__ == '__main__':
    run_tasks()
