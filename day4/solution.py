#!/usr/bin/env python3
import os
import hashlib

from common.utils import get_input_as_string, get_input_as_list

TEST_INPUT = os.path.join(os.path.dirname(__file__), "input/test.in") 
INPUT = os.path.join(os.path.dirname(__file__), "input/input.in")

def day4_part1():
    input = get_input_as_string(INPUT)
    answer = 0
    while True:
        s = input + str(answer)
        md5_hash = hashlib.md5(s.encode()).hexdigest()
        print("{} md5 hash is {}".format(s, md5_hash), end='\r')
        if md5_hash.startswith("00000"):
            print("")
            return answer
        answer += 1

def day4_part2():
    input = get_input_as_string(INPUT)
    answer = 0
    while True:
        s = input + str(answer)
        md5_hash = hashlib.md5(s.encode()).hexdigest()
        if md5_hash.startswith("000000"):
            print("")
            return answer
        print("{} md5 hash is {}".format(s, md5_hash), end='\r')
        answer += 1
