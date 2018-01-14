#!/usr/bin/env python3
# http://adventofcode.com/2017

import math
import itertools
from functools import lru_cache
from collections import Counter
from pprint import pprint
import copy
import csv
import operator
import logging as log
import os
import sys
import pytest

LOGLEVEL = os.environ.get('LOGLEVEL', 'WARNING').upper()
log.basicConfig(level=LOGLEVEL)


def spinlock(steps):
    a = [0]
    current_position = 0
    for value in range(1, 2018):
        current_position = (current_position + steps) % len(a)
        a.insert(current_position+1, value)
        current_position += 1
    return a

        
def part1():
    final_list = spinlock(348)
    needed_value = final_list[final_list.index(2017) + 1]
    print(needed_value)


def part2():
    pass



def main():
    part1()
    part2()


if __name__ == '__main__':
    sys.exit(main())
