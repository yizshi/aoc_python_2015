#!/usr/bin/env python3
import os
import numpy as np
from itertools import chain

from common.utils import get_input_as_string, get_input_as_list

"""
grid:

(0,0)       (999,0)




(999,0)    (999,999)


"""


TEST_INPUT = os.path.join(os.path.dirname(__file__), "input/test.in") 
INPUT = os.path.join(os.path.dirname(__file__), "input/input.in")

def day6_part1():
    input = get_input_as_list(INPUT)

    N = 1000
    grid = [[0] * N for _ in range(N)]
    # print(np.matrix(grid))
    
    for line in input:
        *_ ,start , _ ,end  = line.split(" ")
        if line.startswith("turn on"):
            grid = turn_on(grid, start, end)
        if line.startswith("turn off"):
            grid = turn_off(grid, start, end)
        if line.startswith("toggle"):
            grid = toggle(grid, start, end)
    result = count_on(grid)
    # print(np.matrix(grid))
    return result

def day6_part2():
    input = get_input_as_list(INPUT)

    N = 1000
    grid = [[0] * N for _ in range(N)]
    # print(np.matrix(grid))
    
    for line in input:
        *_ ,start , _ ,end  = line.split(" ")
        if line.startswith("turn on"):
            grid = turn_up(grid, start, end)
        if line.startswith("turn off"):
            grid = turn_down(grid, start, end)
        if line.startswith("toggle"):
            grid = toggle_two(grid, start, end)
    result = count_on(grid)
    # print(np.matrix(grid))
    return result


def turn_on(grid, start, end):
    s1, s2, e1, e2 = get_start_end(start, end)
    for i in range(s1, e1 + 1):
        for j in range(s2, e2 + 1):
            grid[j][i] = 1
    return grid

def turn_off(grid, start, end):
    s1, s2, e1, e2 = get_start_end(start, end)
    for i in range(s1, e1 + 1):
        for j in range(s2, e2 + 1):
            grid[j][i] = 0
    return grid

def toggle(grid, start, end):
    s1, s2, e1, e2 = get_start_end(start, end)
    for i in range(s1, e1 + 1):
        for j in range(s2, e2 + 1):
            grid[j][i] = 0 if grid[j][i] == 1 else 1
    return grid

def get_start_end(start, end):
    s1, s2 = start.split(",")
    e1, e2 = end.split(",")
    return int(s1), int(s2), int(e1), int(e2)

def count_on(grid):
    total = 0
    unzip_lst = zip(*grid)
    for i in unzip_lst:
        for j in i:
            total += j
    return total

def turn_up(grid, start, end):
    s1, s2, e1, e2 = get_start_end(start, end)
    for i in range(s1, e1 + 1):
        for j in range(s2, e2 + 1):
            grid[j][i] += 1
    return grid

def turn_down(grid, start, end):
    s1, s2, e1, e2 = get_start_end(start, end)
    for i in range(s1, e1 + 1):
        for j in range(s2, e2 + 1):
            grid[j][i] -= 1
            if grid[j][i] < 0:
                grid[j][i] = 0
    return grid

def toggle_two(grid, start, end):
    s1, s2, e1, e2 = get_start_end(start, end)
    for i in range(s1, e1 + 1):
        for j in range(s2, e2 + 1):
            grid[j][i] += 2
    return grid