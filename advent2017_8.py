#!/usr/bin/env python3
# http://adventofcode.com/2017

import math
from itertools import cycle, dropwhile, permutations
from functools import lru_cache
from collections import Counter
from pprint import pprint
import copy
from anytree import Node, RenderTree, LevelOrderGroupIter, PreOrderIter, PostOrderIter
import csv
import logging as log
import os

LOGLEVEL = os.environ.get('LOGLEVEL', 'WARNING').upper()
log.basicConfig(level=LOGLEVEL)


def condition(r, a, n):
    if a == '>':
        return registers[r] > n
    elif a == '<':
        return registers[r] < n
    elif a == '==':
        return registers[r] == n
    elif a == '!=':
        return registers[r] != n
    elif a == '>=':
        return registers[r] >= n
    elif a == '<=':
        return registers[r] <= n


def action(r, a, n):
    if a == 'inc':
        registers[r] += n
    else:
        registers[r] -= n


def main(s):
    if condition(s['cond_register'], s['cond_action'], int(s['cond_number'])):
        action(s['register'], s['action'], int(s['number']))


if __name__ == '__main__':
    node_list = []
    registers = dict()
    all_time_max = 0
    with open('input_advent2017_8.txt') as file:
        # with open('temp') as file:
        reader = csv.DictReader(file, delimiter=' ', fieldnames=[
                                "register",
                                "action",
                                "number",
                                "if",
                                "cond_register",
                                "cond_action",
                                "cond_number"])
        for row in reader:
            registers[row["register"]] = 0
        file.seek(0)
        for row in reader:
            main(row)
            if all_time_max < max(registers.values()):
                all_time_max = max(registers.values())
    print(max(registers.values()), all_time_max)

    # print(node_list)
