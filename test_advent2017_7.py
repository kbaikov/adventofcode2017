import pytest

from advent2017_7 import is_consistent


@pytest.mark.parametrize(
    "input, expected",
    [({1: 2, 2: 2, 3: 2, 4: 2}, True), ({1: 2, 2: 2, 3: 3, 4: 2}, False)],
)
def test_is_consistent(input, expected):
    assert is_consistent(input) == expected
