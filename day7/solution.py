#!/usr/bin/env python3
import os

from common.utils import get_input_as_string, get_input_as_list
from time import sleep
TEST_INPUT = os.path.join(os.path.dirname(__file__), "input/test.in") 
INPUT = os.path.join(os.path.dirname(__file__), "input/input.in")

global solved 
solved = {}
wires = {}

def day7_part1():
    input = get_input_as_list(INPUT)
    for line in input:
        operition, wire = line.split(' -> ')
        wires[wire.strip()] = operition.strip().split(' ')
    
    return calculate("a")


def calculate(wire):
    try:
        return int(wire)
    except ValueError:
        pass

    if wire not in solved:
        ops = wires[wire]
        if len(ops) == 1:
            result = calculate(ops[0])
        else:
            op = ops[-2]
            if op == 'AND':
              result = calculate(ops[0]) & calculate(ops[2])
            elif op == 'OR':
              result = calculate(ops[0]) | calculate(ops[2])
            elif op == 'NOT':
              result = ~calculate(ops[1]) & 0xffff
            elif op == 'RSHIFT':
              result = calculate(ops[0]) >> calculate(ops[2])
            elif op == 'LSHIFT':
              result = calculate(ops[0]) << calculate(ops[2])

        solved[wire] = result
    
    return solved[wire] 


    


def day7_part2():
    # wires should all be the same.
    # so first just get a value
    value_a = day7_part1()
    wires["b"] = ['{}'.format(value_a)]
    global solved 
    solved = {}
    return calculate("a")