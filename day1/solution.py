#!/usr/bin/env python3
import os

from common.utils import get_input_as_string

TEST_INPUT = os.path.join(os.path.dirname(__file__), "input/test.in") 
INPUT = os.path.join(os.path.dirname(__file__), "input/input.in") 
def day1_part1():
    input = get_input_as_string(INPUT)
    floor = 0
    for i in input:
        if i == "(":
            floor += 1
        elif i == ")":
            floor -= 1
    return floor

def day1_part2():
    input = get_input_as_string(INPUT)
    floor = 0
    for i, x in enumerate(input):
        if x == "(":
            floor += 1
        elif x == ")":
            floor -= 1
        if floor < 0:
            return i + 1

