#!/usr/bin/env python3
import os

from common.utils import get_input_as_string, get_input_as_list

TEST_INPUT = os.path.join(os.path.dirname(__file__), "input/test.in")
INPUT = os.path.join(os.path.dirname(__file__), "input/input.in")

def day20_part1():
    input = 34000000 / 10

    present = 0
    house = 0

    while present < input:
        house = house + 1
        present = sum(list(get_divisors(house)))
        # print("checking house: ", house, "with present: ", present)

    return house

def day20_part2():
    input = 34000000 / 11

    present = 0
    house = 831500

    while present < input:
        house = house + 1
        present = sum(list(get_divisors(house))[-50:])
        # print("checking house: ", house, "with present: ", present)

    return house

def get_divisors(n):
    for i in range(1, int(n / 2) + 1):
        if n % i == 0:
            yield i
    yield n
