#!/usr/bin/env python3
# http://adventofcode.com/2017

import math
import itertools
from functools import lru_cache
from collections import Counter, defaultdict, deque
from pprint import pprint
import csv
import logging as log
import os
import pytest

LOGLEVEL = os.environ.get("LOGLEVEL", "WARNING").upper()
log.basicConfig(level=LOGLEVEL)


@pytest.mark.parametrize(
    "input, expected",
    [
        (
            ([("set", "i", "31")], {"i": 0, "pointer": 0, "result": 0}),
            ([("set", "i", "31")], {"i": 31, "pointer": 1, "result": 0}),
        ),
        (
            ([("set", "i", "a")], {"a": 57, "i": 0, "pointer": 0, "result": 0}),
            ([("set", "i", "a")], {"a": 57, "i": 57, "pointer": 1, "result": 0}),
        ),
        (
            ([("add", "i", "31")], {"i": 2, "pointer": 0, "result": 0}),
            ([("add", "i", "31")], {"i": 33, "pointer": 1, "result": 0}),
        ),
        (
            ([("add", "i", "a")], {"a": 2, "i": 3, "pointer": 0, "result": 0}),
            ([("add", "i", "a")], {"a": 2, "i": 5, "pointer": 1, "result": 0}),
        ),
        (
            ([("mul", "i", "31")], {"i": 2, "pointer": 0, "result": 0}),
            ([("mul", "i", "31")], {"i": 62, "pointer": 1, "result": 0}),
        ),
        (
            ([("mul", "i", "a")], {"a": 2, "i": 2, "pointer": 0, "result": 0}),
            ([("mul", "i", "a")], {"a": 2, "i": 4, "pointer": 1, "result": 0}),
        ),
        (
            ([("mod", "i", "10")], {"i": 31, "pointer": 0, "result": 0}),
            ([("mod", "i", "10")], {"i": 1, "pointer": 1, "result": 0}),
        ),
        (
            ([("mod", "i", "a")], {"a": 10, "i": 31, "pointer": 0, "result": 0}),
            ([("mod", "i", "a")], {"a": 10, "i": 1, "pointer": 1, "result": 0}),
        ),
        (
            ([("snd", "i")], {"a": 10, "i": 31, "pointer": 0, "result": 0}),
            ([("snd", "i")], {"a": 10, "i": 31, "pointer": 1, "result": 31}),
        ),
        (
            ([("jgz", "i", "10")], {"i": 0, "pointer": 0, "result": 0}),
            ([("jgz", "i", "10")], {"i": 0, "pointer": 1, "result": 0}),
        ),
        (
            ([("jgz", "i", "10")], {"i": 1, "pointer": 0, "result": 0}),
            ([("jgz", "i", "10")], {"i": 1, "pointer": 10, "result": 0}),
        ),
        (
            ([("jgz", "i", "a")], {"a": 10, "i": 1, "pointer": 0, "result": 0}),
            ([("jgz", "i", "a")], {"a": 10, "i": 1, "pointer": 10, "result": 0}),
        ),
        (
            ([("jgz", "i", "a")], {"a": -5, "i": 1, "pointer": 0, "result": 0}),
            ([("jgz", "i", "a")], {"a": -5, "i": 1, "pointer": -5, "result": 0}),
        ),
        (
            (
                [("rcv", "i")],
                {"a": 10, "i": 1, "pointer": 0, "result": 0, "end_program": None},
            ),
            (
                [("rcv", "i")],
                {"a": 10, "i": 1, "pointer": 0, "result": 0, "end_program": True},
            ),
        ),
        (
            (
                [("rcv", "i")],
                {"a": 10, "i": 0, "pointer": 0, "result": 0, "end_program": None},
            ),
            (
                [("rcv", "i")],
                {"a": 10, "i": 0, "pointer": 1, "result": 0, "end_program": None},
            ),
        ),
    ],
)
def test_process(input, expected):
    assert process(*input) == expected


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


def process2(instructions, registers):
    try:
        operation, X, Y = instructions[registers["pointer"]]
    except ValueError:
        operation, X = instructions[registers["pointer"]]

    if operation == "snd":
        pass

    if operation == "rcv":
        pass

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

    # A class variable, counting the number of robots
    queue0 = deque.deque()

    def __init__(self, id):
        """Initializes the data."""
        self.id = id
        registers = defaultdict(int)
        registers["pointer"] = 0
        registers["result"] = 0
        registers["end_program"] = None
        registers["p"] = self.id
        print("(Initializing {0})".format(self.id))

        # When this person is created, the robot
        # adds to the population
        Robot.population += 1

    def __del__(self):
        """I am dying."""
        print("{0} is being destroyed!".format(self.id))

        

    def snd(self):
        """send"""
        print("Greetings, my masters call me {0}.".format(self.id))

    def rcv():
        """receive"""
        print("We have {0:d} robots.".format(Robot.population))

    howMany = staticmethod(howMany)


if __name__ == "__main__":
    # registers = defaultdict(int)
    # registers["pointer"] = 0
    # registers["result"] = 0
    # registers["end_program"] = None
    # with open("input_advent2017_18.txt") as file:
    #     instructions = [tuple(line.split()) for line in file.readlines()]

    instructions = [tuple(line.split()) for line in TEST_INSTRUCTIONS2.splitlines()]
    program0 = Program(0)
    program1 = Program(1)
    # while not registers["end_program"]:
    #     instructions, registers = process(instructions, registers)
    # print(instructions, registers["result"])
