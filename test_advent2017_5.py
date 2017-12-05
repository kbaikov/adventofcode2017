import pytest

from advent2017_5 import process, process_3_or_more


@pytest.mark.parametrize("input, expected", [
    ({1: 0, 2: 3, 3: 0, 4: 1, 5: -3}, 5),
])
def test_process(input, expected):
    assert process(input) == expected


@pytest.mark.parametrize("input, expected", [
    ({1: 0, 2: 3, 3: 0, 4: 1, 5: -3}, 10),
])
def test_process_3_or_more(input, expected):
    assert process_3_or_more(input) == expected
