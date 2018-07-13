import pytest

from advent2017_1 import advent_sum, advent_half_list_sum


@pytest.mark.parametrize(
    "input, expected", [("1122", 3), ("1111", 4), ("1234", 0), ("91212129", 9)]
)
def test_advent_sum(input, expected):
    assert advent_sum(input) == expected


@pytest.mark.parametrize(
    "input, expected",
    [("1212", 6), ("1221", 0), ("123425", 4), ("123123", 12), ("12131415", 4)],
)
def test_advent_half_list_sum(input, expected):
    assert advent_half_list_sum(input) == expected
