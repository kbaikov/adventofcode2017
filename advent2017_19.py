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


labyrinth = [line for line in TEST_INSTRUCTIONS.splitlines()]


def make_a_step(x, y, direction):
    global labyrinth
    if direction == "east":
        return (x, y + 1, labyrinth[x][y + 1])
    elif direction == "north":
        return (x - 1, y, labyrinth[x - 1][y])
    elif direction == "west":
        return (x, y - 1, labyrinth[x][y - 1])
    elif direction == "south":
        return (x + 1, y, labyrinth[x + 1][y])


def next_direction(x, y, direction):
    global labyrinth
    if direction in ["east", "west"]:
        try:
            next = labyrinth[x + 1][y]
        except IndexError:
            next = None
        if next:
            return x + 1, y, "south"
        else:
            return x - 1, y, "north"
    else:
        try:
            next = labyrinth[x][y + 1]
        except IndexError:
            next = None
        if next:
            return x, y + 1, "east"
        else:
            return x, y - 1, "west"


def parse(start_x, start_y, start_direction):
    s = ['|']
    x, y, char = make_a_step(start_x, start_y, start_direction)
    direction = start_direction
    while True:
        x, y, char = make_a_step(x, y, direction)
        s.append(char)
        if char == '+':
            _, _, direction = next_direction(x, y, direction)
        log.debug(s)
    return s

if __name__ == "__main__":

    # with open("input_advent2017_19.txt") as file:
    #     instructions = [line for line in file.readlines()]
    start_y = TEST_INSTRUCTIONS.index("|")
    print(parse(0, start_y, 'south'))
