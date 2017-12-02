#!/usr/bin/env python3
# http://adventofcode.com/2017


def difference(row):
    l = []
    for item in row.split():
        l.append(int(item))
    return max(l) - min(l)


def evenly_divided(row):
    from itertools import permutations
    for pair in permutations(row.split(), 2):
        if int(pair[0]) % int(pair[1]) == 0:
            return int(pair[0]) / int(pair[1])


if __name__ == '__main__':
    with open('input_advent2017_2.txt') as file:
        checksum = checksumdiv = 0
        for line in file:
            checksum += difference(line.strip())
            checksumdiv += evenly_divided(line.strip())
        print(checksum)
        print(checksumdiv)
