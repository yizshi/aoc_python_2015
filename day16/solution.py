#!/usr/bin/env python3
import os
import re

from common.utils import get_input_as_string, get_input_as_list

TEST_INPUT = os.path.join(os.path.dirname(__file__), "input/test.in") 
INPUT = os.path.join(os.path.dirname(__file__), "input/input.in")

gift_aunt = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}

anuts = {}

def day16_part1():
    get_sues()
    for gift_key, gift_value in gift_aunt.items():
        for anut in list(anuts.keys()):
            anut_mfcsam = anuts[anut]
            for item, value in anut_mfcsam.items():
                if item == gift_key and value != gift_value:
                    del anuts[anut]
                    continue

    return list(anuts.keys())[0]

def day16_part2():
    get_sues()
    for gift_key, gift_value in gift_aunt.items():
        for anut in list(anuts.keys()):
            anut_mfcsam = anuts[anut]
            for item, value in anut_mfcsam.items():
                if item in ["cats","trees"]:
                    if item == gift_key and value <= gift_value:
                        del anuts[anut]
                        continue
                elif item in ["pomeranians","goldfish"]:
                    if item == gift_key and value >= gift_value:
                        del anuts[anut]
                        continue
                elif item == gift_key and value != gift_value:
                    del anuts[anut]
                    continue
    return list(anuts.keys())[0]

def get_sues():
    input = get_input_as_list(INPUT)
    for line in input:
        p = re.compile(r'^Sue ([0-9]+): ([A-Za-z]+): ([0-9]+), ([A-Za-z]+): ([0-9]+), ([A-Za-z]+): ([0-9]+)$')
        sue, item1, number1, item2, number2, item3, number3 = p.findall(line)[0]
        anuts[sue] = {
            item1: int(number1),
            item2: int(number2),
            item3: int(number3),
        }