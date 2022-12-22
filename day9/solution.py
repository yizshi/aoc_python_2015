#!/usr/bin/env python3
import os
import sys
from itertools import permutations 
import json

from common.utils import get_input_as_string, get_input_as_list

TEST_INPUT = os.path.join(os.path.dirname(__file__), "input/test.in") 
INPUT = os.path.join(os.path.dirname(__file__), "input/input.in")

def day9_part1():
    distance_between_cities = {}
    route_with_distance = {}
    input = get_input_as_list(INPUT)
    for line in input:
        cities, distance = line.split(" = ")
        distance = int(distance)
        city_1 , city_2 = cities.split(" to ")
        if city_1 not in distance_between_cities.keys():
            distance_between_cities[city_1] = {city_2: distance}
        else:
            distance_between_cities[city_1].update({city_2: distance})
        if city_2 not in distance_between_cities.keys():
            distance_between_cities[city_2] = {city_1: distance}
        else:
            distance_between_cities[city_2].update({city_1: distance})
    min_distance = sys.maxsize
    for route in list(permutations(distance_between_cities.keys())):
        route_distance = 0
        for i in range(1, len(route)):
            route_distance += distance_between_cities[route[i-1]][route[i]]
        
        min_distance = min(min_distance, route_distance)
        route_with_distance.update({route: route_distance})

    # for key, value in route_with_distance.items():
    #     print(key, " : ", value)
    return min_distance

def day9_part2():
    distance_between_cities = {}
    route_with_distance = {}
    input = get_input_as_list(INPUT)
    for line in input:
        cities, distance = line.split(" = ")
        distance = int(distance)
        city_1 , city_2 = cities.split(" to ")
        if city_1 not in distance_between_cities.keys():
            distance_between_cities[city_1] = {city_2: distance}
        else:
            distance_between_cities[city_1].update({city_2: distance})
        if city_2 not in distance_between_cities.keys():
            distance_between_cities[city_2] = {city_1: distance}
        else:
            distance_between_cities[city_2].update({city_1: distance})
    max_distance = 0
    for route in list(permutations(distance_between_cities.keys())):
        route_distance = 0
        for i in range(1, len(route)):
            route_distance += distance_between_cities[route[i-1]][route[i]]
        
        max_distance = max(max_distance, route_distance)
        route_with_distance.update({route: route_distance})

    # for key, value in route_with_distance.items():
    #     print(key, " : ", value)
    return max_distance
