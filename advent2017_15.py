#!/usr/bin/env python3
# http://adventofcode.com/2017

import math
from itertools import cycle, dropwhile, permutations, accumulate
from functools import lru_cache, reduce
from collections import Counter, namedtuple
from pprint import pprint
import copy
import csv
import operator
import logging as log
import os
import sys

puzzle_input = """ 
    Generator A starts with 634
    Generator B starts with 301
    """


def genarator(starting_value, factor):
    while True:
        starting_value = yield (starting_value * factor) % 2147483647


def picky_genarator(starting_value, factor, divider):
    """from https://stackoverflow.com/questions/34075575/using-yield-from-with-conditional-in-python"""
    gen = genarator(starting_value, factor)
    val = next(gen)
    while True:
        if val % divider == 0:
            received = yield val
            val = gen.send(received)
        else:
            val = gen.send(val)


def part1():
    start_A = 634
    factor_A = 16807
    A = genarator(start_A, factor_A)
    A.send(None)

    start_B = 301
    factor_B = 48271
    B = genarator(start_B, factor_B)
    B.send(None)

    matches = 0
    for _ in range(40000000):
        start_A = A.send(start_A)
        start_B = B.send(start_B)
        if bin(start_A)[-16:] == bin(start_B)[-16:]:
            matches += 1
    print(matches)


def part2():
    start_A = 634
    factor_A = 16807
    divider_A = 4
    A = picky_genarator(start_A, factor_A, divider_A)
    A.send(None)

    start_B = 301
    factor_B = 48271
    divider_B = 8
    B = picky_genarator(start_B, factor_B, divider_B)
    B.send(None)

    matches = 0
    for _ in range(5000000):
        start_A = A.send(start_A)
        start_B = B.send(start_B)
        if bin(start_A)[-16:] == bin(start_B)[-16:]:
            matches += 1
    print(matches)


def main():
    # part1()
    part2()


if __name__ == "__main__":
    sys.exit(main())
