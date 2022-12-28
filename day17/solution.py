#!/usr/bin/env python3
import os
from itertools import combinations 

from common.utils import get_input_as_string, get_input_as_list

TEST_INPUT = os.path.join(os.path.dirname(__file__), "input/test.in") 
INPUT = os.path.join(os.path.dirname(__file__), "input/input.in")

def day17_part1():
    containers = get_input_as_list(INPUT)
    containers = list(map(int, containers))
    combos = 0
    for i in range(len(containers)):
        for combo in combinations(containers, i):
            if sum(combo) == 150:
                combos += 1

    return combos

def day17_part2():
    containers = get_input_as_list(INPUT)
    containers = list(map(int, containers))
    for i in range(len(containers)):
        combos = 0
        for combo in combinations(containers, i):
            if sum(combo) == 150:
                combos += 1
        if combos:
            return combos

    # return combos
