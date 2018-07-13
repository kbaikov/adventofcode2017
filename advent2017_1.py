#!/usr/bin/env python3
# http://adventofcode.com/2017


def advent_sum(a):
    matches = []
    for i, item in enumerate(a[:-1]):
        if item == a[i + 1]:
            matches.append(int(item))
    if a[-1] == a[0]:
        matches.append(int(a[-1]))
    return (sum(matches))


def advent_half_list_sum(a):
    matches = []
    half = len(a) // 2
    for i, item in enumerate(a):
        if i < half:
            if item == a[half + i]:
                matches.append(int(item))
        else:
            if item == a[i - half]:
                matches.append(int(item))
    # if a[-1] == a[0]:
    #     matches.append(int(a[-1]))
    return (sum(matches))


if __name__ == "__main__":
    with open("input_advent2017_1.txt") as file:
        for line in file:
            print(advent_sum((line.strip())))
            print(advent_half_list_sum((line.strip())))
    # print(advent_half_list_sum("1221"))
