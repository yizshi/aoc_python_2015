#!/usr/bin/env python3
import os

from common.utils import get_input_as_string, get_input_as_list

TEST_INPUT = os.path.join(os.path.dirname(__file__), "input/test.in") 
INPUT = os.path.join(os.path.dirname(__file__), "input/input.in")

def day11_part1():
    password = list(get_input_as_string(INPUT))
    while not check_password_security(password):
        incremente(password)
    return "".join(password)
    # print(_double_repeat(list("hxbxxwxy")))


def day11_part2():
    password = list(day11_part1())
    password = incremente(password)
    while not check_password_security(password):
        incremente(password)
    return "".join(password)

def incremente(old_password, place = -1):
    char_to_incremente = old_password[place]
    if char_to_incremente == 'z':
        old_password[place] = 'a'
        incremente(old_password, place= place-1)
    else:
        old_password[place] = chr(ord(old_password[place]) + 1)
    return old_password

def check_password_security(password):
    if not _three_letter(password):
        return False

    if _include_letter(password, "i"):
        return False
    if _include_letter(password, "o"):
        return False
    if _include_letter(password, "l"):
        return False

    if not _double_repeat(password):
        return False
    
    return True

def _include_letter(password, letter):
    return letter in password

def _double_repeat(password):
    repeated = 0
    c1 = password[0]
    last_repeated = False
    for char in password[1:]:
        if last_repeated:
            last_repeated = False
            c1 = char
            continue
        if c1 == char:
            repeated += 1
            last_repeated = True
        else:
            c1 = char
    return repeated > 1

def _three_letter(password):
    c1 = password[0]
    c2 = password[1]
    for char in password[2:]:
        if ord(char) - ord(c2) == 1 and ord(c2) - ord(c1) == 1:
            return True
        c1 = c2
        c2 = char
    return False