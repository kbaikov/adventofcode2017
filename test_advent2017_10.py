import pytest

from advent2017_10 import insert_from, select_reverse, one_round, knot_hash


@pytest.mark.parametrize("input, expected", [
    ((1, [1, 2, 3], [3, 4, 5, 6]), [3, 1, 2, 3]),
    ((0, [1, 2, 3], [3, 4, 5, 6]), [1, 2, 3, 6]),
    ((2, [1, 2, 3], [3, 4, 5, 6]), [3, 4, 1, 2]),
    ((3, [1, 2, 3], [3, 4, 5, 6]), [2, 3, 5, 1]),
])
def test_insert_from(input, expected):
    assert insert_from(*input) == expected


@pytest.mark.parametrize("input, expected", [
    ((1, 2, [3, 4, 5, 6]), [5, 4]),
    ((0, 3, [3, 4, 5, 6]), [5, 4, 3]),
    ((2, 3, [3, 4, 5, 6]), [3, 6, 5]),
    ((3, 3, [3, 4, 5, 6]), [4, 3, 6]),
])
def test_select_reverse(input, expected):
    assert select_reverse(*input) == expected


@pytest.mark.parametrize("input, expected", [
    ('', 'a2582a3a0e66e6e86e3812dcb672a272'),
    ('AoC 2017', '33efeb34ea91902bb2f59c9920caa6cd'),
    ('1,2,3', '3efbe78a8d82f29979031a4aa0b16a9d'),
    ('1,2,4', '63960835bcdc130f0b66d7ff4f6a5a8e'),
])
def test_knot_hash(input, expected):
    assert knot_hash(input) == expected

@pytest.mark.parametrize("input, expected", [
    (([3, 4, 1, 5], 0, 0, [0, 1, 2, 3, 4]), ([3, 4, 2, 1, 0], 4, 4)),
])
def test_one_round(input, expected):
    assert one_round(*input) == expected
