#!/usr/bin/env python3
# http://adventofcode.com/2017

import math
from itertools import cycle, dropwhile, permutations
from functools import lru_cache
from collections import Counter
from pprint import pprint
import copy
from anytree import Node, RenderTree, LevelOrderGroupIter, PreOrderIter, PostOrderIter
import csv



def difference(s):
    l = list(s.values())
    return max(l) - min(l)


if __name__ == '__main__':
    node_list = []
    registers = dict()
    cond_registers = dict()
    with open('temp') as file:
        reader = csv.DictReader(file, delimiter=' ', fieldnames=["register", "action", "number", "if", "cond_register", "comp_action", "comp_number"])
        for row in reader:
            registers[row["register"]] = 0
            cond_registers[row["cond_register"]] = 0
    print(registers)

    # print(node_list)
