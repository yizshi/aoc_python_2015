#!/usr/bin/env python3
import os
import re

from common.utils import get_input_as_string, get_input_as_list

TEST_INPUT = os.path.join(os.path.dirname(__file__), "input/test.in") 
INPUT = os.path.join(os.path.dirname(__file__), "input/input.in")

def day14_part1():
    input = get_input_as_list(INPUT)
    TOTAL_TIME = 2503
    reindeers = {}
    for line in input:
        name = line.split(" ")[0]
        speed, run_time, rest_time = re.findall("\d+", line)
        reindeers[name] = (
            {"speed": int(speed), 
            "run_time": int(run_time),
            "rest_time": int(rest_time)
            })
    max_distance = 0
    for reindeer in reindeers.values():
        # print(reindeer)
        distance = calc_distance(
            TOTAL_TIME, 
            reindeer["speed"], 
            reindeer["run_time"],
            reindeer["rest_time"])
        # print(distance)
        max_distance = max(max_distance, distance)

    return max_distance

def day14_part2():
    input = get_input_as_list(INPUT)
    TOTAL_TIME = 2503
    reindeers = {}
    reindeers_distance = {}
    for line in input:
        name = line.split(" ")[0]
        speed, run_time, rest_time = re.findall("\d+", line)
        reindeers[name] = (
            {"speed": int(speed), 
            "run_time": int(run_time),
            "rest_time": int(rest_time),
            "score": 0
            })
        reindeers_distance[name] = 0
    for time in range(1, TOTAL_TIME + 1):
        for name, reindeer in reindeers.items():
            distance = calc_distance(
                time, 
                reindeer["speed"], 
                reindeer["run_time"],
                reindeer["rest_time"])
            reindeers_distance[name] = distance
        winner_distance = max(reindeers_distance.values())
        for name in reindeers.keys():
            if reindeers_distance[name] == winner_distance:
                reindeers[name]["score"] += 1 
    max_scores = 0
    for name in reindeers.keys():
        max_scores = max(max_scores, reindeers[name]["score"])
    return max_scores

def calc_distance(total_time, speed, run_time, rest_time):
    total_run_time = 0
    total_run_time += (total_time//(run_time + rest_time)) * run_time
    # print(total_run_time)
    total_run_time += min(run_time, total_time%(run_time + rest_time))

    total_distance = speed * total_run_time

    return total_distance