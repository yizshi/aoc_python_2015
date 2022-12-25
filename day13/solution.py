#!/usr/bin/env python3
import os
from itertools import permutations 

from common.utils import get_input_as_string, get_input_as_list

TEST_INPUT = os.path.join(os.path.dirname(__file__), "input/test.in") 
INPUT = os.path.join(os.path.dirname(__file__), "input/input.in")

def day13_part1():
    input = get_input_as_list(INPUT)
    happiness = {}
    for line in input:
        line = line.replace("would gain ","")
        line = line.replace("would lose ","-")
        line = line.replace("happiness units by sitting next to ", "")
        p1, hap, p2 = line.split(" ")
        p2 = p2[:-1]
        hap = int(hap)
        if not happiness.get(p1):
            happiness[p1] = {p2: hap}
        else:
            happiness[p1][p2] = hap
    max_happiness = 0
    for seats in permutations(happiness.keys()):
        change = 0
        for i in range(len(seats)):
            if i == 0:
                change += happiness[seats[i]][seats[len(seats)-1]]
                change += happiness[seats[i]][seats[i+1]]
            elif i == len(seats)-1:
                change += happiness[seats[i]][seats[0]]
                change += happiness[seats[i]][seats[i-1]]
            else:
                change += happiness[seats[i]][seats[i+1]]
                change += happiness[seats[i]][seats[i-1]]

        max_happiness = max(max_happiness, change)
        
    return max_happiness

def day13_part2():
    input = get_input_as_list(INPUT)
    happiness = {}
    for line in input:
        line = line.replace("would gain ","")
        line = line.replace("would lose ","-")
        line = line.replace("happiness units by sitting next to ", "")
        p1, hap, p2 = line.split(" ")
        p2 = p2[:-1]
        hap = int(hap)
        if not happiness.get(p1):
            happiness[p1] = {p2: hap}
        else:
            happiness[p1][p2] = hap
    old_keys = happiness.keys()
    for key in list(old_keys):
        happiness[key]["You"] = 0
        if not happiness.get("You"):
            happiness["You"] = {key: 0}
        else:
            happiness["You"][key] = 0
    max_happiness = 0
    for seats in permutations(happiness.keys()):
        change = 0
        for i in range(len(seats)):
            if i == 0:
                change += happiness[seats[i]][seats[len(seats)-1]]
                change += happiness[seats[i]][seats[i+1]]
            elif i == len(seats)-1:
                change += happiness[seats[i]][seats[0]]
                change += happiness[seats[i]][seats[i-1]]
            else:
                change += happiness[seats[i]][seats[i+1]]
                change += happiness[seats[i]][seats[i-1]]

        max_happiness = max(max_happiness, change)
        
    return max_happiness
