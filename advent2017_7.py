#!/usr/bin/env python3
# http://adventofcode.com/2017

import math
from itertools import cycle, dropwhile, permutations
from functools import lru_cache
from collections import Counter
from pprint import pprint
import copy
from anytree import Node, RenderTree
import csv


def create_nodes(s):
    try:
        node, value, _, *children = s
        for i, child in enumerate(children):
            children[i] = child.replace(",", "")
        globals()[node] = Node(node)
        node_list.append(node)
    except ValueError as e:
        node, value = s
        globals()[node] = Node(node)
        node_list.append(node)


def assign_children(s):
    try:
        node, value, _, *children = s
        for i, child in enumerate(children):
            children[i] = child.replace(",", "")
        node.children = children
    except:
        pass


def main(bank):
    pass


if __name__ == '__main__':
    node_list = []
    initial = dict()
    with open('temp') as file:
        reader = csv.reader(file, delimiter=' ')
        for row in reader:
            create_nodes(row)
            assign_children(row)
    print(node_list)
    print(ugml.children)
    print(RenderTree(ugml))
    # print(initial)
    # print(main(initial))
    # print(main({1:0, 2:2, 3:7, 4:0}))


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
