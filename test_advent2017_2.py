import pytest

from advent2017_2 import evenly_divided, difference


@pytest.mark.parametrize(
    "input, expected", [("5 1 9 5", 8), ("7 5 3", 4), ("2 4 6 8", 6)]
)
def test_difference(input, expected):
    assert difference(input) == expected


@pytest.mark.parametrize(
    "input, expected", [("5 9 2 8", 4), ("9 4 7 3", 3), ("3 8 6 5", 2)]
)
def test_evenly_divided(input, expected):
    assert evenly_divided(input) == expected
