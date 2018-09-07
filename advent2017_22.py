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
    grid = None
    directions = deque(["up", "right", "down", "left"])

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.direction = Carrier.directions[0]
        self.infections = 0

    def get_new_direction(self):
        if Carrier.grid[self.y][self.x] == "#":
            Carrier.directions.rotate(-1)
            self.direction = Carrier.directions[0]
        else:
            Carrier.directions.rotate(1)
            self.direction = Carrier.directions[0]

    def infect_clean(self):
        if Carrier.grid[self.y][self.x] == "#":
            Carrier.grid[self.y][self.x] = "."
        else:
            Carrier.grid[self.y][self.x] = "#"
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
    carrier_X = carrier_Y = len(lines[0]) // 2 + 1
    Carrier.grid = lines
    # Carrier.grid[carrier_Y][carrier_X - 1] = "#"
    # Carrier.grid[carrier_Y - 1][carrier_X + 1] = "#"
    c = Carrier(carrier_X, carrier_Y)
    number_of_bursts = 300
    # pprint(lines, width=80, depth=80)
    for _ in range(number_of_bursts):
        c.burst()
    # pprint(Carrier.grid)

    for line in Carrier.grid:
        print("".join(line))

