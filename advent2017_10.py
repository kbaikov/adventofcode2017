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

LOGLEVEL = os.environ.get("LOGLEVEL", "WARNING").upper()
log.basicConfig(level=LOGLEVEL)


def insert_from(place, from_l, to_l):
    for i, item in enumerate(from_l):
        try:
            to_l[i + place] = item
        except IndexError:
            to_l[i + place - len(to_l)] = item
    return to_l


def select_reverse(place, length, to_l):
    if place + length < len(to_l):
        return list(reversed(to_l[place:place + length]))
    else:
        p = length - len(to_l[place:])
        return list(reversed(to_l[place:] + to_l[:p]))


def one_round(length_sequence, current_position, skip_size, init_list):
    for length in length_sequence:
        result_list = insert_from(
            current_position,
            select_reverse(current_position, length, init_list),
            init_list,
        )
        current_position += length + skip_size
        if current_position >= len(result_list):
            current_position = current_position % len(result_list)
        skip_size += 1
        if skip_size >= len(result_list):
            skip_size = skip_size % len(result_list)
    return result_list, current_position, skip_size


def knot_hash(input_string):
    mega_list = list(range(256))
    current_position = 0
    skip_size = 0
    lengths = [ord(i) for i in input_string]
    lengths.extend([17, 31, 73, 47, 23])
    for i in range(64):
        mega_list, current_position, skip_size = one_round(
            lengths, current_position, skip_size, mega_list
        )
    chunks = [mega_list[x:x + 16] for x in range(0, len(mega_list), 16)]
    dense_hash = [list(accumulate(chunk, func=operator.xor))[-1] for chunk in chunks]
    hash_string = "".join([format(x, "02x") for x in dense_hash])
    return hash_string


def part1():
    mega_list = list(range(256))
    with open("input_advent2017_10.txt") as file:
        lengths = [int(x) for x in file.readline().strip().split(",")]
        result_list, _, _ = one_round(lengths, 0, 0, mega_list)
    print(result_list[0] * result_list[1])


def part2():
    with open("input_advent2017_10.txt") as file:
        input_string = file.readline().strip()

    print(knot_hash(input_string))


def main():
    part1()
    part2()


if __name__ == "__main__":
    sys.exit(main())
