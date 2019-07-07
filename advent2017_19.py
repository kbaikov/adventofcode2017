#!/usr/bin/env python3
# http://adventofcode.com/2017

import math
import itertools
from functools import lru_cache
from collections import Counter, defaultdict
from pprint import pprint
import csv
import logging as log
import os
import pytest
import queue

LOGLEVEL = os.environ.get("LOGLEVEL", "DEBUG").upper()
log.basicConfig(level=LOGLEVEL)


TEST_INSTRUCTIONS = """     |          
     |  +--+    
     A  |  C    
 F---|----E|--+ 
     |  |  |  D 
     +B-+  +--+
"""


def make_a_step(x, y, direction, labyrinth):
    if direction == "east":
        return (x, y + 1, labyrinth[x][y + 1])
    elif direction == "north":
        return (x - 1, y, labyrinth[x - 1][y])
    elif direction == "west":
        return (x, y - 1, labyrinth[x][y - 1])
    elif direction == "south":
        return (x + 1, y, labyrinth[x + 1][y])


def next_direction(x, y, direction, labyrinth):
    if direction in ["east", "west"]:
        try:
            next = labyrinth[x + 1][y]
        except IndexError:
            next = None
        if next and next not in ' ':
            return x + 1, y, "south"
        else:
            return x - 1, y, "north"
    else:
        try:
            next = labyrinth[x][y + 1]
        except IndexError:
            next = None
        if next and next not in ' ':
            return x, y + 1, "east"
        else:
            return x, y - 1, "west"


def parse(start_x, start_y, start_direction, labyrinth):
    s = ['|']
    x, y, char = make_a_step(start_x, start_y, start_direction, labyrinth)
    direction = start_direction
    while True:
        try:
            x, y, char = make_a_step(x, y, direction, labyrinth)
        except IndexError:
            break
        s.append(char)
        if char == '+':
            _, _, direction = next_direction(x, y, direction, labyrinth)
        if char == ' ':
            break
    log.debug(s)
    return s

if __name__ == "__main__":

    with open("input_advent2017_19.txt") as file:
        instructions = [line for line in file.readlines()]
    # instructions = labyrinth = [line for line in TEST_INSTRUCTIONS.splitlines()]
    labyrinth = instructions
    # start_y = TEST_INSTRUCTIONS.index("|")
    start_y = instructions[0].index("|")
    full_path = parse(0, start_y, 'south', labyrinth)
    print(''.join([x for x in full_path if x.isalpha()]), len(full_path))

# LOHMDQATP
