#!/usr/bin/env python3
# http://adventofcode.com/2017

import math
from itertools import cycle, dropwhile
from functools import lru_cache

sides = ["east", "north", "west", "south"]
visited = dict()
visited[(0, 0)] = "east", 1
visited[(1, 0)] = "east", 1


def can_go_left(x, y, direction, visited):
    if direction == "east":
        if (x, y + 1) in visited:
            return False
        else:
            return True
    elif direction == "north":
        if (x - 1, y) in visited:
            return False
        else:
            return True
    elif direction == "west":
        if (x, y - 1) in visited:
            return False
        else:
            return True
    elif direction == "south":
        if (x + 1, y) in visited:
            return False
        else:
            return True


def make_a_step(x, y, direction):
    if direction == "east":
        return (x + 1, y)
    elif direction == "north":
        return (x, y + 1)
    elif direction == "west":
        return (x - 1, y)
    elif direction == "south":
        return (x, y - 1)


def next_direction(direction):
    c = cycle(sides)
    skipped = dropwhile(lambda x: x != direction, c)
    next(skipped)
    return next(skipped)


def sum_adjacent(x, y, visited):
    s = 0
    for adj in (x - 1, y - 1), (x, y - 1), (x + 1, y - 1),\
            (x - 1, y),  (x + 1, y),\
            (x - 1, y + 1), (x, y + 1), (x + 1, y + 1):
        try:
            _, temp = visited[adj]
            s += temp
        except KeyError as e:
            pass
    return s


def spiral(n):
    if n == 0:
        return 0, 0, "east", 1
    if n == 1:
        return 1, 0, 'east', 1
    if n > 1:
        for i in range(n - 1):
            (x, y), (direction, s) = visited.popitem()
            visited[(x, y)] = direction, s
            if can_go_left(x, y, direction, visited):
                new_direction = next_direction(direction)
                new_x, new_y = make_a_step(x, y, new_direction)
                visited[(new_x, new_y)] = new_direction, sum_adjacent(
                    new_x, new_y, visited)
            else:
                new_x, new_y = make_a_step(x, y, direction)
                visited[(new_x, new_y)] = direction, sum_adjacent(
                    new_x, new_y, visited)
        print(visited)
        return list(visited.items())[-1]


if __name__ == '__main__':
    value = 0
    n = 3
    while value <= 361527:
        (x, y), (direction, value) = spiral(n)
        n += 1
    print(value)
