#!/usr/bin/env python3
# http://adventofcode.com/2017

import math
from itertools import groupby
from functools import lru_cache
from collections import Counter, defaultdict, deque
from pprint import pprint
import csv
import logging as log
import os
import pytest
import queue
import re

LOGLEVEL = os.environ.get("LOGLEVEL", "DEBUG").upper()
log.basicConfig(level=LOGLEVEL)


class Carrier:
    grid = defaultdict(lambda: ".")
    directions = deque(["up", "right", "down", "left"])

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.direction = Carrier.directions[0]
        self.infections = 0

    def current_possition_value(self):
        return Carrier.grid[(self.x, self.y)]

    def get_new_direction(self):
        if self.current_possition_value() == "#":
            Carrier.directions.rotate(-1)
            self.direction = Carrier.directions[0]
        elif self.current_possition_value() == ".":
            Carrier.directions.rotate(1)
            self.direction = Carrier.directions[0]

    def infect_clean(self):
        if self.current_possition_value() == "#":
            Carrier.grid[(self.x, self.y)] = "."
        elif self.current_possition_value() == ".":
            Carrier.grid[(self.x, self.y)] = "#"
            self.infections += 1

    def move(self):
        if self.direction == "up":
            self.y -= 1
        elif self.direction == "right":
            self.x += 1
        elif self.direction == "down":
            self.y += 1
        elif self.direction == "left":
            self.x -= 1

    def burst(self):
        self.get_new_direction()
        log.debug(f"New direction is {self.direction}")
        self.infect_clean()
        log.debug(f"Current infections {self.infections}")
        self.move()
        log.debug(f"Current coordinates x = {self.x}; y = {self.y}")


if __name__ == "__main__":

    with open("input_advent2017_22.txt") as file:
        lines = [list(line.strip()) for line in file.readlines()]
    # grid_X = grid_Y = 1500
    for y, li in enumerate(lines):
        for x, char in enumerate(li):
            Carrier.grid[(x, y)] = char

    print(Carrier.grid)
    # Carrier.grid = lines
    # Carrier.grid = massage(Carrier.grid, 6)
    carrier_X = len(lines) // 2
    carrier_Y = len(lines) // 2
    # Carrier.grid[carrier_Y][carrier_X - 1] = "#"
    # Carrier.grid[carrier_Y - 1][carrier_X + 1] = "#"
    c = Carrier(carrier_X, carrier_Y)
    number_of_bursts = 10_000
    # pprint(lines, width=80, depth=80)
    for _ in range(number_of_bursts):
        # for line in Carrier.grid:
        #     print("".join(line))
        c.burst()
    # pprint(Carrier.grid)

    # not 6046
    # not 5017
    # a = [["a"], ["b"]]
    # print(massage(a, 1))
