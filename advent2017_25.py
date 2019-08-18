#!/usr/bin/env python3
# http://adventofcode.com/2017

# solution copied from  https://github.com/norvig/pytudes/blob/master/ipynb/Advent%202017.ipynb


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

LOGLEVEL = os.environ.get("LOGLEVEL", "INFO").upper()
log.basicConfig(level=LOGLEVEL)


def machine():
    "machine()[state][value] == (new_value, move, new_state)}"
    L, R = -1, +1
    A, B, C, D, E, F = "ABCDEF"
    return {
        A: [(1, R, B), (0, R, F)],
        B: [(0, L, B), (1, L, C)],
        C: [(1, L, D), (0, R, C)],
        D: [(1, L, E), (1, R, A)],
        E: [(1, L, F), (0, L, D)],
        F: [(1, R, A), (0, L, E)],
    }


def turing(machine, state, steps):
    "Run the Turing machine for given number of steps, then return tape."
    tape = defaultdict(int)
    cursor = 0
    for step in range(steps):
        tape[cursor], move, state = machine[state][tape[cursor]]
        cursor += move
    return tape


if __name__ == "__main__":
    print(sum(turing(machine(), "A", 12425180).values()))

