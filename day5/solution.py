#!/usr/bin/env python3
import os

from common.utils import get_input_as_string, get_input_as_list

TEST_INPUT = os.path.join(os.path.dirname(__file__), "input/test.in") 
INPUT = os.path.join(os.path.dirname(__file__), "input/input.in")

def day5_part1():
    input = get_input_as_list(INPUT)
    nice_string_count = 0
    for line in input:
        count_vowels = 0
        two_letter_in_a_row = False
        naughty_string = False
        prev_char = ""
        for char in line:
            if check_one(char):
                count_vowels += 1
            if check_two(prev_char, char):
                two_letter_in_a_row = True
            if check_three(prev_char, char):
                naughty_string = True
            prev_char = char
        if count_vowels >= 3 and two_letter_in_a_row and not naughty_string:
            nice_string_count += 1
                    
    return nice_string_count

def day5_part2():
    input = get_input_as_list(INPUT)
    nice_string_count = 0
    for line in input:
        prev = ""
        before_prev = ""
        has_repeat = False
        pair = []
        has_pair = False
        for i, char in enumerate(line):
            if not has_pair:
                if (prev, char) in pair:
                    # print("here")
                    if i - pair.index((prev, char)) > 1:
                        has_pair = True
                pair.append((prev, char))
            if not has_repeat and check_five(before_prev, char):
                has_repeat = True
            before_prev = prev
            prev = char
        if has_pair and has_repeat:
            nice_string_count += 1
        # print(pair)

    return nice_string_count

def check_one(char):
    if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
        return True

def check_two(prev, curr):
    if prev == curr:
        return True

def check_three(prev, curr):
    if prev == "a":
        return curr == "b"
    if prev == "c":
        return curr == "d"
    if prev == "p":
        return curr == "q"
    if prev == "x":
        return curr == "y"

def check_five(prev, curr):
    if prev == curr:
        return True

