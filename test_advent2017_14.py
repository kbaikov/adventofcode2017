import pytest

from advent2017_14 import to_bin, part1, part2


@pytest.mark.parametrize(
    "input, expected", [("e", "1110"), ("f", "1111"), ("0", "0000")]
)
def test_to_bin(input, expected):
    assert to_bin(input) == expected


@pytest.mark.parametrize("input, expected", [("flqrgnkx", 8108)])
def test_part1(input, expected):
    assert part1(input) == expected


@pytest.mark.parametrize("input, expected", [("flqrgnkx", 1242)])
def test_part2(input, expected):
    assert part2(input) == expected
