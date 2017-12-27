#!/usr/bin/env python3
# http://adventofcode.com/2017

import math
from itertools import cycle, dropwhile, permutations, accumulate
from functools import lru_cache
from collections import Counter
from pprint import pprint
import copy
import csv
import operator
import logging as log
import os
import sys

LOGLEVEL = os.environ.get('LOGLEVEL', 'WARNING').upper()
log.basicConfig(level=LOGLEVEL)


def make_a_step(x, y, z, direction):
    """From https://www.redblobgames.com/grids/hexagons/"""
    if direction == "ne":
        return (x + 1, y, z - 1)
    elif direction == "n":
        return (x, y + 1, z - 1)
    elif direction == "sw":
        return (x - 1, y, z + 1)
    elif direction == "s":
        return (x, y - 1, z + 1)
    elif direction == "nw":
        return (x - 1, y + 1, z)
    elif direction == "se":
        return (x + 1, y - 1, z)


def distance_to_origin(x, y, z):
    return max(abs(x), abs(y), abs(z))


def main():
    x = y = z = 0
    all_distances = []
    with open('input_advent2017_11.txt') as file:
        for direction in file.readline().strip().split(","):
            x, y, z = make_a_step(x, y, z, direction)
            all_distances.append(distance_to_origin(x, y, z))
    print(distance_to_origin(x, y, z), max(all_distances))


if __name__ == '__main__':
    sys.exit(main())
