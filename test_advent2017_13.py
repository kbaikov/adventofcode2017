import pytest

from advent2017_13 import cycle_scanner, process_step, part1, part2

d0 = {0: (['S', None, None], True),
     1: (['S', None], True),
     2: None,
     3: None,
     4: (['S', None, None, None], True),
     5: None,
     6: (['S', None, None, None], True)}

d1 = {0: ([None, 'S', None], True),
                  1: ([None, 'S'], True),
                  2: None,
                  3: None,
                  4: ([None, 'S', None, None], True),
                  5: None,
                  6: ([None, 'S', None, None], True)}


@pytest.mark.parametrize("input, expected", [
    ((0, d0), (True, d1)),
])
def test_process_step(input, expected):
    assert process_step(*input) == expected


@pytest.mark.parametrize("input, expected", [
    (d0, (2, 24)),
])
def test_part1(input, expected):
    assert part1(input) == expected


@pytest.mark.parametrize("input, expected", [
    (d0, 10),
])
def test_part2(input, expected):
    assert part2(input) == expected


@pytest.mark.parametrize("input, expected", [
    (([None, None, "S", None], True), ([None, None, None, "S"], True)),
    (([None, None, None, "S"], True), ([None, None, "S", None], False)),
    (([None, None, "S", None], False), ([None, "S", None, None], False)),
    ((["S", None, None, None], False), ([None, "S", None, None], True)),
])
def test_cycle_scanner(input, expected):
    assert cycle_scanner(*input) == expected
