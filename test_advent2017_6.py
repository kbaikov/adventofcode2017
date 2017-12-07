import pytest

from advent2017_6 import redistribute


@pytest.mark.parametrize("input, expected", [
    ({1:0, 2:2, 3:7, 4:0}, {1:2, 2:4, 3:1, 4:2}),
])
def test_redistribute(input, expected):
    assert redistribute(input) == expected

