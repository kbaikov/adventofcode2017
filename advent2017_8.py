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

LOGLEVEL = os.environ.get("LOGLEVEL", "WARNING").upper()
log.basicConfig(level=LOGLEVEL)


def condition(r, a, n, registers):
    if a == ">":
        return registers[r] > n
    elif a == "<":
        return registers[r] < n
    elif a == "==":
        return registers[r] == n
    elif a == "!=":
        return registers[r] != n
    elif a == ">=":
        return registers[r] >= n
    elif a == "<=":
        return registers[r] <= n


def action(r, a, n, registers):
    if a == "inc":
        registers[r] += n
    else:
        registers[r] -= n
    return registers


if __name__ == "__main__":
    node_list = []
    registers = dict()
    all_time_max = 0
    with open("input_advent2017_8.txt") as file:
        # with open('temp') as file:
        reader = csv.DictReader(
            file,
            delimiter=" ",
            fieldnames=[
                "register",
                "action",
                "number",
                "if",
                "cond_register",
                "cond_action",
                "cond_number",
            ],
        )
        for row in reader:
            registers[row["register"]] = 0
        file.seek(0)
        for row in reader:
            if condition(
                row["cond_register"],
                row["cond_action"],
                int(row["cond_number"]),
                registers,
            ):
                registers = action(
                    row["register"], row["action"], int(row["number"]), registers
                )
            if all_time_max < max(registers.values()):
                all_time_max = max(registers.values())
    print(max(registers.values()), all_time_max)

    # print(node_list)
