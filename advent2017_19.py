#!/usr/bin/env python3
# http://adventofcode.com/2017

import math
import itertools
from functools import lru_cache
from collections import Counter, defaultdict
from pprint import pprint
import csv
import logging as log
import os
import pytest
import queue

LOGLEVEL = os.environ.get("LOGLEVEL", "WARNING").upper()
log.basicConfig(level=LOGLEVEL)


TEST_INSTRUCTIONS = """
     |          
     |  +--+    
     A  |  C    
 F---|----E|--+ 
     |  |  |  D 
     +B-+  +--+
"""


if __name__ == "__main__":

    with open("input_advent2017_19.txt") as file:
        instructions = [line for line in file.readlines()]
