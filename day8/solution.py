#!/usr/bin/env python3
import os
import re

from common.utils import get_input_as_string, get_input_as_list

TEST_INPUT = os.path.join(os.path.dirname(__file__), "input/test.in") 
INPUT = os.path.join(os.path.dirname(__file__), "input/input.in")

def day8_part1():
    lines = get_input_as_list(INPUT)
    string_literals = 0
    chars_memory = 0
    for line in lines:
        string_literals += len(line)

        # first remove two ""
        string_teardown = line[1:-1]
        # remove any double backslash with any two char
        string_teardown = re.sub(r'\\\\', "-", string_teardown)
        # remove any escapted quote with any one char
        string_teardown = re.sub(r'\\"', "-", string_teardown)
        # remove any ASCII char (\x12) with any one char
        string_teardown = re.sub(r'\\x[0-9a-f]{2}', "-", string_teardown)
        # print(string_teardown)
        chars_memory += len(string_teardown)

    
    return string_literals - chars_memory

def day8_part2():
    lines = get_input_as_list(INPUT)
    string_literals = 0
    new_string = 0
    for line in lines:
        string_literals += len(line)

        string_encode = re.sub(r'"','---', line)
        string_encode = re.sub(r'\\x[0-9a-f]{2}', "-----", string_encode)
        string_encode = re.sub(r'\\"', "----", string_encode)
        string_encode = re.sub(r'\\\\', "----", string_encode)
        new_string += len(string_encode)
    
    return new_string - string_literals
