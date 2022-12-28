#!/usr/bin/env python3
import os
from collections import Counter
from itertools import chain
import copy
from pprint import pprint

from common.utils import get_input_as_string, get_input_as_list

TEST_INPUT = os.path.join(os.path.dirname(__file__), "input/test.in") 
INPUT = os.path.join(os.path.dirname(__file__), "input/input.in")

def day18_part1():
    STEPS = 100
    input = get_input_as_list(INPUT)
    grid = []
    for line in input:
        grid.append(list(line))
    for _ in range(STEPS):
        grid = animate(grid)

    total_on = Counter(chain(*grid))["#"]
    return total_on

def day18_part2():
    STEPS = 100
    input = get_input_as_list(INPUT)
    grid = []
    for line in input:
        grid.append(list(line))
    for _ in range(STEPS):
        grid = animate(grid)

    total_on = Counter(chain(*grid))["#"]
    return total_on

def animate(grid):
    new_grid = copy.deepcopy(grid)
    for x, line in enumerate(grid):
        for y, dot in enumerate(line):
            if dot == ".":
                new_grid[x][y] = _off_check(grid, x, y)
            if dot == "#":
                new_grid[x][y] = _on_check(grid, x, y)
    new_grid[0][0] = "#"
    new_grid[0][len(new_grid[x])-1] = "#"
    new_grid[len(new_grid)-1][0] = "#"
    new_grid[len(new_grid)-1][len(new_grid[x])-1] = "#"
    
    return new_grid


def _on_check(grid, x, y):
    surround = _check_neighbors(grid, x, y)
    if surround == 2 or surround == 3:
        return "#"
    return "."

def _off_check(grid, x, y):
    surround = _check_neighbors(grid, x, y)
    if surround == 3:
        return "#"
    return "."

def _check_neighbors(grid, x, y):
    surround = 0

    if x == 0 and y == 0:
        surround = _check_top_left(grid, x, y)
    elif x == 0 and y == len(grid[x]) - 1:
        surround = _check_top_right(grid, x, y)
    elif x == len(grid) - 1 and y == 0:
        surround = _check_bottom_left(grid, x, y)
    elif x == len(grid) - 1 and y == len(grid[x]) - 1:
        surround = _check_bottom_right(grid, x, y)
    elif x == 0:
        surround = _check_top(grid, x, y)
    elif x == len(grid) - 1:
        surround = _check_bottom(grid, x, y)
    elif y == 0:
        surround = _check_left(grid, x, y)
    elif y == len(grid[x]) - 1:
        surround += _check_right(grid, x, y)
    else:
        surround = _check_all_neighbors(grid, x, y)
    
    return surround

def _check_all_neighbors(grid, x, y):
    on = Counter([
        grid[x-1][y-1],
        grid[x][y-1],
        grid[x+1][y-1],
        grid[x-1][y],
        grid[x+1][y],
        grid[x-1][y+1],
        grid[x][y+1],
        grid[x+1][y+1],    
    ])["#"]
    return on

def _check_top_left(grid, x, y):
    on = Counter([
        grid[x+1][y],
        grid[x][y+1],
        grid[x+1][y+1],
    ])["#"]
    return on

def _check_top_right(grid, x, y):
    on = Counter([
        grid[x][y-1],
        grid[x+1][y-1],
        grid[x+1][y]
    ])["#"]
    return on

def _check_bottom_left(grid, x, y):
    on = Counter([
        grid[x-1][y],
        grid[x-1][y+1],
        grid[x][y+1],
    ])["#"]
    return on

def _check_bottom_right(grid, x, y):
    on = Counter([
        grid[x-1][y-1],
        grid[x-1][y],
        grid[x][y-1],
    ])["#"]
    return on

"""
    [x-1][y-1]  |   [x-1][y]    |   [x-1][y+1]
    [x][y-1]    |   [x][y]      |   [x][y+1]
    [x+1][y-1]  |   [x+1][y]    |   [x+1][y+1]
"""
def _check_bottom(grid, x, y):
    on = Counter([
        grid[x][y-1],
        grid[x][y+1],
        grid[x-1][y-1],
        grid[x-1][y],
        grid[x-1][y+1],
    ])["#"]
    return on

def _check_top(grid, x, y):
    on = Counter([
        grid[x][y-1],
        grid[x][y+1],
        grid[x+1][y-1],
        grid[x+1][y],
        grid[x+1][y+1],    
    ])["#"]
    return on

def _check_left(grid, x, y):
    on = Counter([
        grid[x-1][y],
        grid[x+1][y],
        grid[x-1][y+1],
        grid[x][y+1],
        grid[x+1][y+1],     
    ])["#"]
    return on

def _check_right(grid, x, y):
    on = Counter([
        grid[x-1][y],
        grid[x+1][y],
        grid[x-1][y-1],
        grid[x][y-1],
        grid[x+1][y-1],    
    ])["#"]
    return on

