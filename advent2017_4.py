#!/usr/bin/env python3
# http://adventofcode.com/2017

import math
from itertools import cycle, dropwhile, permutations
from functools import lru_cache
from collections import Counter


def no_duplicates(s):
    c = Counter(s.split())
    if all(v == 1 for v in c.values()):
        return True
    else:
        return False


def no_anagrams(s):
    for pair in permutations(s.split(), 2):
        if Counter(pair[0]) == Counter(pair[1]):
            return False
    return True

if __name__ == '__main__':
    num_of_valid = 0
    with open('input_advent2017_4.txt') as file:
        for line in file:
            if no_duplicates(line) and no_anagrams(line):
                num_of_valid +=1
        print(num_of_valid)
