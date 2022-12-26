#!/usr/bin/env python3
import os
import re

from common.utils import get_input_as_string, get_input_as_list

TEST_INPUT = os.path.join(os.path.dirname(__file__), "input/test.in") 
INPUT = os.path.join(os.path.dirname(__file__), "input/input.in")


def day15_part1():
    data = []
    input = get_input_as_list(INPUT)
    for line in input:
        a,b,c,d,e = re.findall("-?\d", line)
        data.append([int(a), int(b), int(c), int(d), int(e)])
    # print(data)

    max_score = 0
    for a in range(0, 101):
        for b in range(0, 101 - a):
            for c in range(0, 101 - a - b):
                d = 100 - a - b - c 
                score = calc_score(data, a, b, c, d)
                max_score = max(max_score, score)


    return max_score

def day15_part2():
    data = []
    input = get_input_as_list(INPUT)
    for line in input:
        a,b,c,d,e = re.findall("-?\d", line)
        data.append([int(a), int(b), int(c), int(d), int(e)])
    # print(data)

    max_score = 0
    for a in range(0, 101):
        for b in range(0, 101 - a):
            for c in range(0, 101 - a - b):
                d = 100 - a - b - c 
                score = calc_score_with_500_cal(data, a, b, c, d)
                max_score = max(max_score, score)

    return max_score


def calc_score(data, a, b, c, d):
    s1 = data[0][0] * a + data[1][0] * b + data[2][0] * c + data[3][0] * d
    if s1<0: return 0
    s2 = data[0][1] * a + data[1][1] * b + data[2][1] * c + data[3][1] * d
    if s2<0: return 0
    s3 = data[0][2] * a + data[1][2] * b + data[2][2] * c + data[3][2] * d
    if s3<0: return 0
    s4 = data[0][3] * a + data[1][3] * b + data[2][3] * c + data[3][3] * d
    if s4<0: return 0

    if s1 < 0 or s2 < 0 or s3 < 0 or s4 < 0:
        return 0
    
    return s1 * s2 * s3 * s4

def calc_score_with_500_cal(data, a, b, c, d):
    cal = data[0][4] * a + data[1][4] * b + data[2][4] * c + data[3][4] * d

    if cal != 500: return -1

    s1 = data[0][0] * a + data[1][0] * b + data[2][0] * c + data[3][0] * d
    if s1<0: return 0
    s2 = data[0][1] * a + data[1][1] * b + data[2][1] * c + data[3][1] * d
    if s2<0: return 0
    s3 = data[0][2] * a + data[1][2] * b + data[2][2] * c + data[3][2] * d
    if s3<0: return 0
    s4 = data[0][3] * a + data[1][3] * b + data[2][3] * c + data[3][3] * d
    if s4<0: return 0
    
    return s1 * s2 * s3 * s4

