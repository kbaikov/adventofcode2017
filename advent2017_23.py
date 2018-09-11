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

LOGLEVEL = os.environ.get("LOGLEVEL", "INFO").upper()
log.basicConfig(level=LOGLEVEL)


def process(instructions, registers):
    try:
        operation, X, Y = instructions[registers["pointer"]]
    except ValueError:
        operation, X = instructions[registers["pointer"]]

    if operation == "snd":
        registers["result"] = registers[X]
        registers["pointer"] += 1

    if operation == "rcv":
        if int(registers[X]) != 0:
            registers["end_program"] = True
        else:
            registers["pointer"] += 1

    if operation == "jgz":
        if int(registers[X]) > 0:
            if Y.lstrip("-").isdigit():
                registers["pointer"] += int(Y)
            else:
                registers["pointer"] += registers[Y]
        else:
            registers["pointer"] += 1

    if operation == "set":
        if Y.lstrip("-").isdigit():
            registers[X] = int(Y)
        else:
            registers[X] = registers[Y]
        registers["pointer"] += 1

    if operation == "add":
        if Y.lstrip("-").isdigit():
            registers[X] += int(Y)
        else:
            registers[X] += registers[Y]
        registers["pointer"] += 1

    if operation == "mul":
        if Y.lstrip("-").isdigit():
            registers[X] *= int(Y)
        else:
            registers[X] *= registers[Y]
        registers["pointer"] += 1

    if operation == "mod":
        if Y.lstrip("-").isdigit():
            registers[X] %= int(Y)
        else:
            registers[X] %= registers[Y]
        registers["pointer"] += 1

    return instructions, registers


TEST_INSTRUCTIONS = """set a 1
add a 2
mul a a
mod a 5
snd a
set a 0
rcv a
jgz a -1
set a 1
jgz a -2
"""

TEST_INSTRUCTIONS2 = """snd 1
snd 2
snd p
rcv a
rcv b
rcv c
rcv d
"""


class Program:
    """
    Represents a program, with an id.
    With the  help of https://github.com/nedbat/adventofcode2017/blob/master/day18.py
    """

    def __init__(self, id, instructions):
        """Initializes the data."""

        self.id = id
        # self.q = queue.Queue()
        self.q = []
        self.pointer = 0
        self.result = 0
        self.end_program = None
        self.X = 0
        self.Y = 0
        self.p = self.id
        self.num_sent = 0
        self.ready = True
        self.mul_times = 0
        self.instructions = [line.split() for line in instructions]
        for value in "abcdefgh":
            setattr(self, value, 0)
        log.debug("Initializing program {0}".format(self.id))

    def process_instruction(self):
        try:
            self.operation, self.X, self.Y = self.instructions[self.pointer]
        except ValueError:
            self.operation, self.X = self.instructions[self.pointer]
        if self.operation == "set":
            self.operation = "set_"
        if self.q:
            self.ready = True
        getattr(self, self.operation)()

    def set_(self):
        if self.Y.lstrip("-").isdigit():
            setattr(self, self.X, int(self.Y))
        else:
            v = getattr(self, self.Y, 0)
            setattr(self, self.X, v)
        self.pointer += 1

    def add(self):
        if self.Y.lstrip("-").isdigit():
            s = getattr(self, self.X, 0)
            setattr(self, self.X, s + int(self.Y))
        else:
            s1 = getattr(self, self.X, 0)
            s2 = getattr(self, self.Y, 0)
            setattr(self, self.X, s1 + s2)
        self.pointer += 1

    def sub(self):
        if self.Y.lstrip("-").isdigit():
            s = getattr(self, self.X, 0)
            setattr(self, self.X, s - int(self.Y))
        else:
            s1 = getattr(self, self.X, 0)
            s2 = getattr(self, self.Y, 0)
            setattr(self, self.X, s1 - s2)
        self.pointer += 1

    def mul(self):
        if self.Y.lstrip("-").isdigit():
            s = getattr(self, self.X, 0)
            setattr(self, self.X, s * int(self.Y))
        else:
            s1 = getattr(self, self.X, 0)
            s2 = getattr(self, self.Y, 0)
            setattr(self, self.X, s1 * s2)
        self.pointer += 1
        self.mul_times += 1

    def mod(self):
        if self.Y.lstrip("-").isdigit():
            s = getattr(self, self.X, 0)
            setattr(self, self.X, s % int(self.Y))
        else:
            s1 = getattr(self, self.X, 0)
            s2 = getattr(self, self.Y, 0)
            setattr(self, self.X, s1 % s2)
        self.pointer += 1

    def jnz(self):
        try:
            x = int(self.X)
        except ValueError:
            x = getattr(self, self.X, 0)
        if not x == 0:
            if self.Y.lstrip("-").isdigit():
                self.pointer += int(self.Y)
            else:
                s = getattr(self, self.Y, 0)
                self.pointer += s
        else:
            self.pointer += 1

    def snd(self):
        """send"""

        if self.X.lstrip("-").isdigit():
            s = int(self.X)
        else:
            s = getattr(self, self.X, 0)
        if self.id == 0:
            program1.q.append(s)
            program1.ready = True
            log.debug(f"sent {s} to program 1")
        else:
            program0.q.append(s)
            program0.ready = True
            program1.num_sent += 1
            log.debug(f"sent {s} to program 0")
        self.pointer += 1

    def rcv(self):
        """receive"""

        if self.q:
            s = self.q.pop(0)
            setattr(self, self.X, int(s))
            log.debug(f"Program {self.id} received {s}.")
            self.pointer += 1
            self.ready = True
        else:
            self.ready = False
            return


if __name__ == "__main__":
    # registers = defaultdict(int)
    # registers["pointer"] = 0
    # registers["result"] = 0
    # registers["end_program"] = None
    with open("input_advent2017_23.txt") as file:
        instructions = [line for line in file.readlines()]

    # instructions = [line for line in TEST_INSTRUCTIONS2.splitlines()]
    log.debug(instructions)
    program0 = Program(0, instructions)
    program1 = Program(1, instructions)
    while True:
        program0.process_instruction()
        print(program0.mul_times)

    # Part1: 4225
