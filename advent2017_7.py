#!/usr/bin/env python3
# http://adventofcode.com/2017

import math
from itertools import cycle, dropwhile, permutations
from functools import lru_cache
from collections import Counter
from pprint import pprint
import copy
import anytree


def main(bank):
    pass

if __name__ == '__main__':
    seen = []
    initial = dict()
    with open('input_advent2017_7.txt') as file:
        for index, line in enumerate(file.readline().strip().split(), 1):
            initial[index] = int(line)
    print(initial)
    print(main(initial))
    # print(main({1:0, 2:2, 3:7, 4:0}))


input = """
pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)
"""
output = """

                gyxo
              /     
         ugml - ebii
       /      \     
      |         jptl
      |        
      |         pbga
     /        /
tknk --- padx - havc
     \        \
      |         qoyq
      |             
      |         ktlj
       \      /     
         fwft - cntj
              \     
                xhth

"""
