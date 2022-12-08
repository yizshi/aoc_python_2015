#!/bin/bash
dir=$(pwd)

if [ "$1" == "" ]; then
  echo "provide folder name to start new days's challange. ex: 'day12' "
  exit 1
fi

if [ ! -d $dir/$1 ]; then
  mkdir -p $dir/$1/input
  touch $dir/$1/input/input.in
  touch $dir/$1/input/test.in
  touch $dir/$1/solution.py
  touch $dir/$1/__init__.py
fi