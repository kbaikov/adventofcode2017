import pytest

from advent2017_11 import distance_to_origin, make_a_step


@pytest.mark.parametrize("input, expected", [
    ((0, 0, 0, 'ne'), (1, 0, -1)),
])
def test_make_a_step(input, expected):
    assert make_a_step(*input) == expected


@pytest.mark.parametrize("input, expected", [
    ((1, 0, -1), 1),
])
def test_distance_to_origin(input, expected):
    assert distance_to_origin(*input) == expected

