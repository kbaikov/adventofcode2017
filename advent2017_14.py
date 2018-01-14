#!/usr/bin/env python3
# http://adventofcode.com/2017

import math
from itertools import cycle, dropwhile, permutations, accumulate
from functools import lru_cache, reduce
from collections import Counter, namedtuple
from pprint import pprint
import copy
import csv
import operator
import logging as log
import os
import sys

LOGLEVEL = os.environ.get('LOGLEVEL', 'WARNING').upper()
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
            select_reverse(
                current_position,
                length,
                init_list),
            init_list)
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
            lengths, current_position, skip_size, mega_list)
    chunks = [mega_list[x:x + 16] for x in range(0, len(mega_list), 16)]
    dense_hash = [list(accumulate(chunk, func=operator.xor))[-1]
                  for chunk in chunks]
    hash_string = "".join([format(x, '02x') for x in dense_hash])
    return hash_string


def to_bin(s):
    return bin(int(s, base=16))[2:].zfill(4)


def part1(s):
    input_rows = [s + '-' + '{}'.format(n) for n in range(128)]
    input_rows_hashes = [knot_hash(i) for i in input_rows]
    input_rows_bin = [''.join(map(to_bin, digits))
                      for digits in input_rows_hashes]
    total_sum = 0
    for row in input_rows_bin:
        total_sum += row.count('1')
    return total_sum


Point = namedtuple('Point', 'x y')


# part2 is from https://dsp.stackexchange.com/questions/2516/counting-the-number-of-groups-of-1s-in-a-boolean-map-of-numpy-array
def points_adjoin(p1, p2):
    # to accept diagonal adjacency, use this form
    # return -1 <= p1.x-p2.x <= 1 and -1 <= p1.y-p2.y <= 1
    return (-1 <= p1.x - p2.x <= 1 and p1.y == p2.y or
            p1.x == p2.x and -1 <= p1.y - p2.y <= 1)


def adjoins(pts, pt):
    return any(points_adjoin(p, pt) for p in pts)


def locate_regions(datastring):
    data = map(list, datastring.splitlines())
    regions = []
    datapts = [Point(x, y)
               for y, row in enumerate(data)
               for x, value in enumerate(row) if value == '1']
    for dp in datapts:
        # find all adjoining regions
        adjregs = [r for r in regions if adjoins(r, dp)]
        if adjregs:
            adjregs[0].add(dp)
            if len(adjregs) > 1:
                # joining more than one reg, merge
                regions[:] = [r for r in regions if r not in adjregs]
                regions.append(reduce(set.union, adjregs))
        else:
            # not adjoining any, start a new region
            regions.append(set([dp]))
    return regions


def part2(s):
    input_rows = [s + '-' + '{}'.format(n) for n in range(128)]
    input_rows_hashes = [knot_hash(i) for i in input_rows]
    input_rows_bin = [''.join(map(to_bin, digits))
                      for digits in input_rows_hashes]
    total_sum = 0
    for row in input_rows_bin:
        total_sum += row.count('1')
    return len(locate_regions('\n'.join(input_rows_bin)))


def main():
    print(part1('nbysizxe'))
    # part2 is from https://dsp.stackexchange.com/questions/2516/counting-the-number-of-groups-of-1s-in-a-boolean-map-of-numpy-array
    print(part2('nbysizxe'))


if __name__ == '__main__':
    sys.exit(main())
