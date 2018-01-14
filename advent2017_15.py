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


def genarator(starting_value, factor):
    while True:
        starting_value = yield (starting_value * factor) % 2147483647


def part1():
    start_A = 65
    factor_A = 16807
    A = genarator(start_A, factor_A)
    A.send(None)

    start_B = 8921
    factor_B = 48271
    B = genarator(start_B, factor_B)
    B.send(None)

    for _ in range(5):
        start_A = A.send(start_A)
        start_B = B.send(start_B)
        print(start_A, start_B)


def main():
    part1()


if __name__ == '__main__':
    sys.exit(main())
