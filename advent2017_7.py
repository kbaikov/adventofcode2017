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


def create_nodes(s):
    try:
        node, value, _, *children = s
        for i, child in enumerate(children):
            children[i] = child.replace(",", "")
        globals()[node] = Node(node, v=eval(value))
        node_list.append(node)
    except ValueError as e:
        node, value = s
        globals()[node] = Node(node, v=eval(value))
        node_list.append(node)


def assign_children(s):
    try:
        node, value, _, *ch = s
        for i, child in enumerate(ch):
            ch[i] = child.replace(",", "")
        children_values = [eval(item) for item in ch]
        globals()[node].children = children_values
    except ValueError:
        pass


def siblings_sum(n):
    result = dict()
    for s in n.siblings:
        result[s] = sum([v.v for v in s.descendants]) + s.v
    result[n] = sum([v.v for v in n.descendants]) + n.v
    return result


def is_consistent(s):
    return all(x == list(s.values())[0] for x in s.values())


def difference(s):
    l = list(s.values())
    return max(l) - min(l)


if __name__ == '__main__':
    node_list = []
    initial = dict()
    with open('input_advent2017_7.txt') as file:
        reader = csv.reader(file, delimiter=' ')
        for row in reader:
            create_nodes(row)
        file.seek(0)
        for row in reader:
            assign_children(row)
    # print(node_list)
    # ugml.children = [gyxo, ebii, jptl]
    # tknk.children = [ugml, padx, fwft]
    # setattr(ugml, "children", [gyxo, ebii, jptl])
    # print(ugml.children)
    tree_root = teuku.root
    # print(RenderTree(tree_root))
    print(tree_root)
    # print(siblings_sum())
    # print(is_consistent(siblings_sum(gyxo)))
    # print([node.name for node in PreOrderIter(tree_root)])
    for node in PreOrderIter(cwwwj):
        if not is_consistent(siblings_sum(node)):
            print(node.name, node.v, siblings_sum(node))
            d = difference(siblings_sum(node))
            print(node.v - d)
    # print(initial)
    # print(main(initial))
    # print(main({1:0, 2:2, 3:7, 4:0}))
