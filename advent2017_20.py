#!/usr/bin/env python3
# http://adventofcode.com/2017

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


class Particle:
    all_particles = {}
    collisions = 0

    def __init__(self, id, s):
        self.id = id
        self.px, self.py, self.pz, self.vx, self.vy, self.vz, self.ax, self.ay, self.az = s
        Particle.all_particles[self] = self.distance

    @property
    def distance(self):
        return abs(self.px) + abs(self.py) + abs(self.pz)

    def simulate(self, number_of_simulations):
        for _ in range(number_of_simulations):
            self.vx += self.ax
            self.vy += self.ay
            self.vz += self.az
            self.px += self.vx
            self.py += self.vy
            self.pz += self.vz

    @classmethod
    def report(cls):
        print(cls.all_particles)

    @classmethod
    def check_unique(cls):
        coords_list = [(p.px, p.py, p.pz) for p in cls.all_particles]
        c = Counter(coords_list)
        log.debug(c)
        unique_coords_list = [x for x in c if c[x] == 1]

        for coord in unique_coords_list:
            for particle in cls.all_particles.copy():
                if coord == (particle.px, particle.py, particle.pz):
                    del cls.all_particles[particle]
        # cls.all_particles = not_collided
        # print(coords_dict.values(), len(coords_dict))
    


if __name__ == "__main__":

    # with open("input_advent2017_20.txt") as file:
    #     lines = [line for line in file.readlines()]

    lines = ["p=<-6,0,0>, v=< 3,0,0>, a=< 0,0,0>", "p=<-4,0,0>, v=< 2,0,0>, a=< 0,0,0>",
    'p=<-2,0,0>, v=< 1,0,0>, a=< 0,0,0>', 'p=< 3,0,0>, v=<-1,0,0>, a=< 0,0,0>']

    # s = re.findall("[-\d]+", line)
    for p_id, particle_string in enumerate(lines, start=0):
        Particle(p_id, [int(n) for n in re.findall("[-\d]+", particle_string)])
    # s = [int(n) for n in re.findall("[-\d]+", line)]
    # p = Particle(1, s)
    # print(p.px, p.manhattan_distance())
    # p.simulate(4)
    # print(p.px, p.manhattan_distance())
    print(len(Particle.all_particles))
    for _ in range(2):
        for en in Particle.all_particles.copy():
            en.simulate(1)
        Particle.check_unique()

    a = sorted(Particle.all_particles, key=lambda particle: particle.distance)
    # print(a[0].id, a[0].distance)
    print(len(Particle.all_particles))
    # print(en.id, en.px, en.manhattan_distance())

