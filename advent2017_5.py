#!/usr/bin/env python3
# http://adventofcode.com/2017

import math
from itertools import cycle, dropwhile, permutations
from functools import lru_cache
from collections import Counter
from pprint import pprint


def process(instructions):
    step_number = 0
    current_index = 1
    next_index = 1
    current_value = instructions[current_index]
    while True:
        try:
            step_number += 1
            current_index = next_index
            jump_value = instructions[current_index]
            instructions[current_index] += 1
            next_index = current_index + jump_value
            current_value = instructions[next_index]
        except (KeyError, IndexError) as e:
            return step_number



if __name__ == '__main__':
    instructions = dict()
    with open('input_advent2017_5.txt') as file:
        for index, line in enumerate(file, 1):
            instructions[index] = int(line.strip())
    # print(process({1:0, 2:3, 3:0, 4:1, 5:-3}))
    print(process(instructions))
