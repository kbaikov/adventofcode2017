#!/usr/bin/env python3
# http://adventofcode.com/2017

# solution copied from  https://github.com/nedbat/adventofcode2017/blob/master/day24.py

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


TEST_DATA = """\
0/2
2/2
2/3
3/4
3/5
0/1
10/1
9/10
"""


def parse_components(lines):
    return [tuple(map(int, line.split("/"))) for line in lines]


def bridges(components, sofar=()):
    last_port = sofar[-1][1] if sofar else 0
    for i, comp in enumerate(components):
        use_comp = None
        if comp[0] == last_port:
            use_comp = comp
        elif comp[1] == last_port:
            use_comp = comp[::-1]
        if use_comp:
            bridge = sofar + (use_comp,)
            yield bridge
            yield from bridges(components[:i] + components[i + 1 :], bridge)


def strength(bridge):
    return sum(sum(pair) for pair in bridge)


def best_bridge(components):
    return max(bridges(components), key=strength)


if __name__ == "__main__":
    with open("input_advent2017_24.txt") as file:
        components = parse_components(file.readlines())
    best = best_bridge(components)
    print(f"Part 1: the strongest bridge has strength {strength(best)}")


def best_bridge2(components):
    """Find the strongest of the longest bridges."""
    return max(bridges(components), key=lambda b: (len(b), strength(b)))


if __name__ == "__main__":
    with open("input_advent2017_24.txt") as file:
        components = parse_components(file.readlines())
    best = best_bridge2(components)
    print(f"Part 2: the strongest longest bridge has strength {strength(best)}")
