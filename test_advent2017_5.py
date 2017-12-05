import pytest

from advent2017_5 import process


@pytest.mark.parametrize("input, expected", [
    ({1: 0, 2: 3, 3: 0, 4: 1, 5: -3}, 5),
])
def test_process(input, expected):
    assert process(input) == expected


