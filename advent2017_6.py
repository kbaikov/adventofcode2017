#!/usr/bin/env python3
# http://adventofcode.com/2017

import math
from itertools import cycle, dropwhile, permutations
from functools import lru_cache
from collections import Counter
from pprint import pprint
import copy


def redistribute(bank):
    max_index = max(bank, key=bank.get)
    max_value = bank[max_index]
    bank[max_index] = 0
    next_index = max_index
    for _ in range(max_value):
        next_index = get_next_index(bank, next_index)
        bank[next_index] += 1

    return bank


def get_next_index(d, i):
    c = cycle(d.keys())
    skipped = dropwhile(lambda x: x != i, c)
    next(skipped)
    return next(skipped)


def main(bank):
    step = 1
    seen.append(bank)
    new_bank = bank.copy()
    while True:
        new_bank = redistribute(copy.deepcopy(new_bank))
        if new_bank in seen:
            step_found = step
            target = copy.deepcopy(new_bank)
            break
        else:
            seen.append(new_bank)
            step += 1

    while True:
        new_bank = redistribute(copy.deepcopy(new_bank))
        if new_bank == target:
            return step, step_found, step - step_found + 1
        else:
            seen.append(new_bank)
            step += 1


if __name__ == "__main__":
    seen = []
    initial = dict()
    with open("input_advent2017_6.txt") as file:
        for index, line in enumerate(file.readline().strip().split(), 1):
            initial[index] = int(line)
    print(initial)
    print(main(initial))
    # print(main({1:0, 2:2, 3:7, 4:0}))
