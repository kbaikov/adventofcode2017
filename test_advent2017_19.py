import pytest

from advent2017_19 import next_direction, make_a_step


@pytest.fixture
def labyrinth():
    from advent2017_19 import TEST_INSTRUCTIONS
    return [line for line in TEST_INSTRUCTIONS.splitlines()]


@pytest.mark.parametrize(
    "input, expected",
    [
        ((1, 8, "north"), (1, 9, "east")),
        ((3, 14, "north"), (3, 13, "west")),
        ((5, 5, "south"), (5, 6, "east")),
        ((5, 8, "east"), (4, 8, "north")),
    ],
)
def test_next_direction(input, expected, labyrinth):
    assert next_direction(*input, labyrinth=labyrinth) == expected


@pytest.mark.parametrize(
    "input, expected",
    [
        ((0, 5, "south"), (1, 5, "|")),
        ((1, 5, "south"), (2, 5, "A")),
        ((2, 5, "south"), (3, 5, "|")),
        ((4, 8, "north"), (3, 8, "-")),
    ],
)
def test_make_a_step(input, expected, labyrinth):
    assert make_a_step(*input, labyrinth=labyrinth) == expected
