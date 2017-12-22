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
    pass

def main():
    with open('input_advent2017_10.txt') as file:
        # print(score_group(clean_garbage(clean_exclamation(file.readline()))))


if __name__ == '__main__':
    sys.exit(main())
