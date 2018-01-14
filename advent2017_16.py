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
import pytest

LOGLEVEL = os.environ.get('LOGLEVEL', 'WARNING').upper()
log.basicConfig(level=LOGLEVEL)


def spin(programs, position):
    programs = programs[-position:] + programs[:-position]
    return programs


@pytest.mark.parametrize("input, expected", [
    ((list('abcde'), 3), list('cdeab')),
])
def test_spin(input, expected):
    assert spin(*input) == expected


def exchange(programs, a, b):
    programs[a], programs[b] = programs[b], programs[a]
    return programs


@pytest.mark.parametrize("input, expected", [
    ((list('abcde'), 0, 1), list('bacde')),
    ((list('abcde'), 4, 2), list('abedc')),
])
def test_exchange(input, expected):
    assert exchange(*input) == expected


def partner(programs, a, b):
    index_A = programs.index(a)
    index_B = programs.index(b)
    return exchange(programs, index_A, index_B)


@pytest.mark.parametrize("input, expected", [
    ((list('abcde'), 'a', 'c'), list('cbade')),
    ((list('abcde'), 'e', 'b'), list('aecdb')),
])
def test_partner(input, expected):
    assert partner(*input) == expected


def process(programs, instructions):
    for instruction in instructions:
        if instruction.startswith('s'):
            programs = spin(programs, int(instruction[1:]))
        elif instruction.startswith('x'):
            a, _, b = instruction[1:].partition('/')
            programs = exchange(programs, int(a), int(b))
        elif instruction.startswith('p'):
            a, _, b = instruction[1:].partition('/')
            programs = partner(programs, a, b)
    return programs


@pytest.mark.parametrize("input, expected", [
    ((list('abcde'), ['s1', 'x3/4', 'pe/b']), list('baedc')),
])
def test_process(input, expected):
    assert process(*input) == expected


def part1():
    with open('input_advent2017_16.txt') as file:
        instructions = file.readline().split(',')
    
    programs = list('abcdefghijklmnop')
    print(''.join(process(programs, instructions)))


def part2():
    with open('input_advent2017_16.txt') as file:
        instructions = file.readline().split(',')
    
    """
    Since i get initial list on iteration 60
    Then the same list as on billions iteration will be
    on 10**9 % 60 = 40 iteration
    """
    programs = list('abcdefghijklmnop')
    for _ in range(40):
        programs = process(programs, instructions)
    print(''.join(programs))


def main():
    # part1()
    part2()


if __name__ == '__main__':
    sys.exit(main())
