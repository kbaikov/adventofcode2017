#!/usr/bin/env python3
# http://adventofcode.com/2017
# copied from https://github.com/nedbat/adventofcode2017/blob/master/day21.py

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
import re

LOGLEVEL = os.environ.get("LOGLEVEL", "DEBUG").upper()
log.basicConfig(level=LOGLEVEL)


def rows_flips(rows):
    yield rows
    yield rows[::-1]
    rrows = [row[::-1] for row in rows]
    yield rrows
    yield rrows[::-1]


def rotations_and_flips(pattern):
    """Given a pattern '../##', produce all the rotations and flips."""
    rows = pattern.split("/")
    size = len(rows)
    assert all(len(rows) == size for row in rows)

    for r in rows_flips(rows):
        yield "/".join(r)

    rot = ["".join(rows[y][x] for y in range(size)) for x in range(size)]
    for r in rows_flips(rot):
        yield "/".join(r)


def read_rules(lines):
    """Returns a dict mapping inputs to outputs, complete."""
    rules = {}
    for line in lines:
        before, _, after = line.strip().partition(" => ")
        for before in rotations_and_flips(before):
            rules[before] = after
    return rules


def slice_grid(gridstring):
    grid = gridstring.split("/")
    gridsize = len(grid)
    assert all(len(row) == gridsize for row in grid)
    return gridsize, grid


def tiles(gridstring, tilesize):
    gridsize, grid = slice_grid(gridstring)
    assert gridsize % tilesize == 0
    for ty in range(gridsize // tilesize):
        for tx in range(gridsize // tilesize):
            rx = tx * tilesize
            ry = ty * tilesize
            yield tx, ty, "/".join(
                grid[y][rx : rx + tilesize] for y in range(ry, ry + tilesize)
            )


def enhance(gridstring, rules):
    gridsize, grid = slice_grid(gridstring)
    if gridsize % 2 == 0:
        tilesize = 2
    else:
        tilesize = 3

    newtilesize = tilesize + 1
    num_rows = gridsize // tilesize * newtilesize
    new_grid = [[None] * (gridsize // tilesize) for _ in range(num_rows)]

    for tx, ty, tilestring in tiles(gridstring, tilesize):
        newtilestring = rules[tilestring]
        for tr, tilerow in enumerate(newtilestring.split("/")):
            new_grid[ty * newtilesize + tr][tx] = tilerow

    return "/".join("".join(row) for row in new_grid)


def run_rules(rules):
    gridstring = ".#./..#/###"
    while True:
        yield gridstring
        gridstring = enhance(gridstring, rules)


def test_run_rules():
    rules = read_rules(["../.# => ##./#../...", ".#./..#/### => #..#/..../..../#..#"])
    expected = [
        ".#./..#/###",
        "#..#/..../..../#..#",
        "##.##./#..#../....../##.##./#..#../......",
    ]
    actual = list(itertools.islice(run_rules(rules), 3))
    assert actual == expected


def on_after(rules, n):
    grid = next(itertools.islice(run_rules(rules), n, None))
    return grid.count("#")


if __name__ == "__main__":
    with open("input_advent2017_21.txt") as finput:
        rules = read_rules(finput)
    print(f"Part 1: after 5 iterations, there are {on_after(rules, 5)} pixels on.")
    print(f"Part 1: after 18 iterations, there are {on_after(rules, 18)} pixels on.")

