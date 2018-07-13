import pytest

from advent2017_3 import next_direction


@pytest.mark.parametrize(
    "input, expected",
    [("east", "north"), ("north", "west"), ("west", "south"), ("south", "east")],
)
def test_next_direction(input, expected):
    assert next_direction(input) == expected
