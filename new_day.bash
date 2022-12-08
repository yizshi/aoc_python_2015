#!/bin/bash
dir=$(pwd)

if [ "$1" == "" ]; then
  echo "provide folder name to start new days's challange. ex: 'day12' "
  exit 1
fi

if [ -d $dir/$1 ]; then
  echo "$1 already exist. Please delete the content before re-create"
  exit 1
fi


mkdir -p $dir/$1/input
touch $dir/$1/input/input.in
touch $dir/$1/input/test.in
touch $dir/$1/solution.py
touch $dir/$1/__init__.py

cat >> $dir/$1/solution.py <<EOF
#!/usr/bin/env python3
import os

from common.utils import get_input_as_string, get_input_as_list

TEST_INPUT = os.path.join(os.path.dirname(__file__), "input/test.in") 
INPUT = os.path.join(os.path.dirname(__file__), "input/input.in")

def $1_part1():
    return 0

def $1_part2():
    return 0
EOF

cat >> $dir/main.py <<EOF

from $1.solution import $1_part1, $1_part2
print("$1 - part 1: {}".format($1_part1()))
print("$1 - part 2: {}".format($1_part2()))
EOF