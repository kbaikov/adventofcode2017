#!/usr/bin/env python3
# http://adventofcode.com/2017

import math
from itertools import groupby
from functools import lru_cache
from collections import Counter, defaultdict
from pprint import pprint
import csv
import logging as log
import os
import pytest
import queue
import re

LOGLEVEL = os.environ.get("LOGLEVEL", "DEBUG").upper()
log.basicConfig(level=LOGLEVEL)


if __name__ == "__main__":

    with open("input_advent2017_21.txt") as file:
        lines = [line for line in file.readlines()]
