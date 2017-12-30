#!/usr/bin/env python3
# http://adventofcode.com/2017

import copy
import csv
import logging as log
import math
import operator
import os
import sys
from collections import Counter
from functools import lru_cache
from itertools import accumulate, cycle, dropwhile, permutations
from pprint import pprint

LOGLEVEL = os.environ.get('LOGLEVEL', 'WARNING').upper()
log.basicConfig(level=LOGLEVEL)


def all_connections(found_connections, node_dict):
    for connection in found_connections.copy():
        for value in node_dict[connection]:
            if value not in found_connections:
                found_connections.add(value)
    return found_connections


def count_groups(node_dict):
    groups_num = 0
    found_connections = set()
    for k in node_dict:
        if k not in found_connections:
            groups_num += 1
            found_connections.add(k)
            for _ in range(200):
                found_connections = all_connections(found_connections, node_dict)
    return groups_num


if __name__ == '__main__':
    node_dict = {}
    with open('input_advent2017_12.txt') as file:
        reader = csv.reader(file, delimiter=' ')
        for row in reader:
            node, _, *children = row
            for i, child in enumerate(children):
                children[i] = child.replace(",", "")
            node_dict[node] = children

    # pprint(node_dict)
    # found_connections = set()
    # found_connections.add('0')
    # for _ in range(20):
    #     found_connections = all_connections(found_connections, node_dict)
    # print(found_connections, len(found_connections))
    print(count_groups(node_dict))
