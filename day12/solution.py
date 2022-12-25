#!/usr/bin/env python3
import os
import re
import json


from common.utils import get_input_as_string, get_input_as_list

TEST_INPUT = os.path.join(os.path.dirname(__file__), "input/test.in") 
INPUT = os.path.join(os.path.dirname(__file__), "input/input.in")

def day12_part1():
    input = get_input_as_string(INPUT)
    all_num_str = re.findall('-?\d+', input)
    sum = 0
    for i in all_num_str:
        sum += int(i)
    return sum

def day12_part2():
    data = json.load(open(INPUT))
    return sumObject(data)
    
def sumObject(obj):
    if type(obj) is int:
        return obj
    
    if type(obj) is list:
        return sum(map(sumObject, obj))
    
    if type(obj) is dict:
        vals = obj.values()
        
        if "red" in vals:
            return 0
        
        return sum(map(sumObject, vals))
    
    else:
        return 0