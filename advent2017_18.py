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

LOGLEVEL = os.environ.get("LOGLEVEL", "WARNING").upper()
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
    """Represents a program, with an id."""

    def __init__(self, id):
        """Initializes the data."""

        self.id = id
        self.q = []
        self.pointer = 0
        self.result = 0
        self.end_program = None
        self.X = 0
        self.Y = 0
        self.p = self.id
        for value in "abcdefgh":
            setattr(self, value, 0)
        print("Initializing program {0}".format(self.id))
    
    def get_instructions(self, instructions):
        self.instructions = instructions
        while not self.end_program:
            self.process_instruction(self.instructions[self.pointer])

    def process_instruction(self, instruction):
        try:
            self.operation, self.X, self.Y = instruction
        except ValueError:
            self.operation, self.X = instruction
        if self.operation == "set":
            self.operation = "set_"
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

    def mul(self):
        if self.Y.lstrip("-").isdigit():
            s = getattr(self, self.X, 0)
            setattr(self, self.X, s * int(self.Y))
        else:
            s1 = getattr(self, self.X, 0)
            s2 = getattr(self, self.Y, 0)
            setattr(self, self.X, s1 * s2)
        self.pointer += 1

    def mod(self):
        if self.Y.lstrip("-").isdigit():
            s = getattr(self, self.X, 0)
            setattr(self, self.X, s % int(self.Y))
        else:
            s1 = getattr(self, self.X, 0)
            s2 = getattr(self, self.Y, 0)
            setattr(self, self.X, s1 % s2)
        self.pointer += 1

    def jgz(self):
        try:
            x = int(self.X)
        except ValueError:
            x = getattr(self, self.X, 0)
        if x > 0:
            if self.Y.lstrip("-").isdigit():
                self.pointer += int(self.Y)
            else:
                s = getattr(self, self, Y, 0)
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
            print("sent {} to program 1".format(s))
        else:
            program0.q.append(s)
            print("sent {} to program 0".format(s))
        self.pointer += 1

    def rcv(self):
        """receive"""

        if not program0.q and not program1.q:
            self.end_program = True
        else:
            if not self.q:
                return
            s = self.q.pop(0)
            setattr(self, self.X, int(s))
            print("receive {}.".format(s))
        self.pointer += 1


if __name__ == "__main__":
    # registers = defaultdict(int)
    # registers["pointer"] = 0
    # registers["result"] = 0
    # registers["end_program"] = None
    # with open("input_advent2017_18.txt") as file:
    #     instructions = [tuple(line.split()) for line in file.readlines()]

    instructions = [tuple(line.split()) for line in TEST_INSTRUCTIONS2.splitlines()]
    print(instructions)
    program0 = Program(0)
    program1 = Program(1)

    # print(program0.q, program1.q)
    # program0.a = 10
    # program0.i = -31
    
    program1.get_instructions([('snd', '1'), ('snd', '2'), ('snd', 'p'), ('rcv', 'a'), ('rcv', 'b'), ('rcv', 'c'), ('rcv', 'd')])
    program0.get_instructions([('snd', '1'), ('snd', '2'), ('snd', 'p'), ('rcv', 'a'), ('rcv', 'b'), ('rcv', 'c'), ('rcv', 'd')])
    
    # program0.process_instruction([("rcv", "a")])
    # program0._set()
    # program0.get_instructions(instructions)
    # program1.get_instructions(instructions)
    print(program0.__dict__)
    print(program0.q, program1.q)

    # while not registers["end_program"]:
    #     instructions, registers = process(instructions, registers)
    # print(instructions, registers["result"])
