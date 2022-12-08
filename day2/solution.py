#!/usr/bin/env python3
import os

from common.utils import get_input_as_list

TEST_INPUT = os.path.join(os.path.dirname(__file__), "input/test.in") 
INPUT = os.path.join(os.path.dirname(__file__), "input/input.in") 
def day2_part1():
    input = get_input_as_list(INPUT)
    total = 0
    for line in input:
        l, w, h = line.split("x")
        l, w, h = int(l), int(w), int(h)
        total += 2*l*w
        total += 2*l*h
        total += 2*w*h
        side_list = [l, w, h]
        side_list.remove(max(side_list))
        total += side_list[0] * side_list[1]
    return total



def day2_part2():
    input = get_input_as_list(INPUT)
    total = 0
    for line in input:
        l, w, h = line.split("x")
        l, w, h = int(l), int(w), int(h)
        side_list = [l, w, h]
        side_list.remove(max(side_list))
        total += 2 * side_list[0] + 2 * side_list[1]
        total += l*w*h
    return total

