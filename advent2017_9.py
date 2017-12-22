#!/usr/bin/env python3
# http://adventofcode.com/2017

import math
from itertools import cycle, dropwhile, permutations
from functools import lru_cache
from collections import Counter
from pprint import pprint
import copy
import csv
import logging as log
import os
import sys

LOGLEVEL = os.environ.get('LOGLEVEL', 'WARNING').upper()
log.basicConfig(level=LOGLEVEL)


def clean_exclamation(s):
    while "!" in s:
        start = s.find('!')
        s = s[:start] + s[start + 2:]
    return s


def clean_garbage(s):
    l = 0
    while '<' in s:
        start = s.find('<')
        end = s.find('>')
        l += len(s[start+1:end])
        s = s[:start] + s[end+1:]
    print(l)
    return s


def score_group(s):
    counter = score = 0
    for char in s:
        if char == "{":
            counter += 1
        if char == "}":
            score += counter
            counter -= 1
    return score


def main():
    with open('input_advent2017_9.txt') as file:
        print(score_group(clean_garbage(clean_exclamation(file.readline()))))


if __name__ == '__main__':
    sys.exit(main())
