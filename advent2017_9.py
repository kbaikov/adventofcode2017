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
    if '!' not in s:
        return s
    if s[0] == '!':
        return clean_exclamation(s[2:])
    return s[0] + clean_exclamation(s[1:])


def main():
    print(clean_exclamation('aaa!ddd!!cc'))
    # with open('input_advent2017_9.txt') as file:


if __name__ == '__main__':
    sys.exit(main())
