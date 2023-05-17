#!/usr/bin/env python3
import os

from common.utils import get_input_as_string, get_input_as_list

TEST_INPUT = os.path.join(os.path.dirname(__file__), "input/test.in") 
INPUT = os.path.join(os.path.dirname(__file__), "input/input.in")

class Location:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_location(self):
        return [self.x, self.y]
    

def day3_part1():
    input = get_input_as_string(INPUT)
    house_cord_list = [[0,0]]
    location = Location(0, 0)

    for i in input:
        if i == "<":
            location.x = location.x - 1
        if i == ">":
            location.x = location.x + 1
        if i == "v":
            location.y = location.y - 1
        if i == "^":
            location.y = location.y + 1
        house_cord_list.append(location.get_location())

    final_list = set(map(lambda i: tuple(i), house_cord_list))

    return len(final_list)

def day3_part2():
    input = get_input_as_string(INPUT)
    santa_house_cord_list = []
    santa_location = Location(0, 0)

    robot_house_cord_list = []
    robot_location = Location(0, 0)

    for i, x in enumerate(input):
        if i%2 != 0:
            if x == "<":
                santa_location.x = santa_location.x - 1
            if x == ">":
                santa_location.x = santa_location.x + 1
            if x == "v":
                santa_location.y = santa_location.y - 1
            if x == "^":
                santa_location.y = santa_location.y + 1
            santa_house_cord_list.append(santa_location.get_location())
        if i%2 == 0:
            if x == "<":
                robot_location.x = robot_location.x - 1
            if x == ">":
                robot_location.x = robot_location.x + 1
            if x == "v":
                robot_location.y = robot_location.y - 1
            if x == "^":
                robot_location.y = robot_location.y + 1
            robot_house_cord_list.append(robot_location.get_location())

    santa_final_list = list(set(map(lambda i: tuple(i), santa_house_cord_list)))
    robot_final_list = list(set(map(lambda i: tuple(i), robot_house_cord_list)))

    for i in robot_final_list:
        santa_final_list.append(i)
    santa_final_list.append([0, 0])
    final_list = set(map(lambda i: tuple(i), santa_final_list))

    return len(final_list)
