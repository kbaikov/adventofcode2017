#!/usr/bin/env python3
# http://adventofcode.com/2017

import copy
import csv
import logging as log
import math
import operator
import os
import sys
from collections import Counter
from functools import lru_cache
from itertools import accumulate, cycle, dropwhile, permutations, count
from pprint import pprint

LOGLEVEL = os.environ.get("LOGLEVEL", "WARNING").upper()
log.basicConfig(level=LOGLEVEL)


def cycle_scanner(le, direction=True):
    l = le.copy()
    current_position = l.index("S")
    l[current_position] = None
    if direction:
        try:
            l[current_position + 1] = "S"
        except IndexError:
            l[current_position - 1] = "S"
            direction = False
    else:
        if current_position == 0:
            l[current_position + 1] = "S"
            direction = True
        else:
            l[current_position - 1] = "S"
    return l, direction


def process_step(packet_position, de):
    d = de.copy()
    caught = False
    if d[packet_position]:
        if d[packet_position][0][0] == "S":
            caught = True
    for k, v in d.items():
        if v:
            d[k] = cycle_scanner(d[k][0], d[k][1])
    return caught, d


def part1(de):
    d = de.copy()
    caught_times = 0
    caught_severity_sum = 0
    for i in range(len(d)):
        caught, d = process_step(i, d)
        if caught:
            caught_times += 1
            caught_severity_sum += i * len(d[i][0])

    return caught_times, caught_severity_sum


def part2(d):
    caught_times = None
    delay = 1
    while caught_times != 0:
        delayed_dict = d.copy()
        delay += 1
        for i in range(delay):
            _, delayed_dict = process_step(0, delayed_dict)
        caught_times, caught_severity_sum = part1(delayed_dict)
    return delay


def caught(delay, d):
    for k, v in d.items():
        if v:
            rng = len(d[k][0])
            if (delay + k) % (2 * (rng - 1)) == 0:
                return True
                break
    return False


def part2_non_brute_force(d):
    """from https://github.com/norvig/pytudes/blob/master/ipynb/Advent%202017.ipynb
       from https://github.com/nedbat/adventofcode2017/blob/master/day13.py"""
    for delay in count(9):
        if not caught(delay, d):
            return delay


if __name__ == "__main__":
    dd = {
        0: (["S", None, None], True),
        1: (["S", None], True),
        2: None,
        3: None,
        4: (["S", None, None, None], True),
        5: None,
        6: (["S", None, None, None], True),
    }
    firewall_dict = dict.fromkeys(range(99))
    with open("input_advent2017_13.txt") as file:
        for line in file:
            k, _, v = line.partition(":")
            firewall_dict[int(k)] = [None for _ in range(int(v))]
    for k, v in firewall_dict.items():
        if v:
            firewall_dict[k] = v, True
            firewall_dict[k][0][0] = "S"
    # print(dd)
    print(part1(firewall_dict))
    # print(part2(firewall_dict))
    print(part2_non_brute_force(firewall_dict))
