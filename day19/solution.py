#!/usr/bin/env python3
import os
import re
from collections import Counter

from common.utils import get_input_as_string, get_input_as_list

TEST_INPUT = os.path.join(os.path.dirname(__file__), "input/test.in") 
INPUT = os.path.join(os.path.dirname(__file__), "input/input.in")

def day19_part1():
    input = get_input_as_list(INPUT)
    replacements = input[:-2]
    input = input[-1]
    machine = {}
    for replacement in replacements:
        x, y = replacement.split(" => ")
        if not machine.get(x):
            machine[x] = [y]
        else:
            machine[x].append(y)
    possible_output = []

    for key in machine.keys():
        for item in machine[key]:
            for i, c in enumerate(input):
                if key == input[i:i+len(key)]:
                    new_string = '{}{}{}'.format(input[:i], item, input[i+len(key):])
                    possible_output.append(new_string)
    return len(set(possible_output))

def day19_part2():
    input = get_input_as_list(INPUT)
    # replacements = input[:-2]
    input = input[-1]
    all_char = re.findall("([A-Z][a-z]?)", input)
    all_occ = Counter(all_char)
    total = all_occ.total()
    parenthesis = all_occ["Rn"] + all_occ["Ar"]
    comma = all_occ["Y"]

    return total - parenthesis - 2*comma - 1
