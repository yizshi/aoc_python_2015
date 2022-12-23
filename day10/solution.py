#!/usr/bin/env python3
import os
from itertools import groupby

from common.utils import get_input_as_string, get_input_as_list

TEST_INPUT = os.path.join(os.path.dirname(__file__), "input/test.in") 
INPUT = os.path.join(os.path.dirname(__file__), "input/input.in")

def day10_part1():
    input = get_input_as_string(INPUT)
    for i in range(40):
        print("calculating {} times of input".format(i), end="\r")
        input = look_and_say(input)
    print()
    return len(input)

def day10_part2():
    input = get_input_as_string(INPUT)
    for i in range(50):
        print("calculating {} times of input".format(i), end="\r")
        input = look_and_say(input)
    print()
    return len(input)

def look_and_say(number):
    new_num = ''
    for key, group in groupby(number):
        new_num = new_num + str(len(list(group))) + key
    return new_num
