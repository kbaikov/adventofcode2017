import pytest

from advent2017_9 import clean_exclamation


@pytest.mark.parametrize("input, expected", [
    ('aaa!ddd!!cc', 'aaaddcc'),
    ('!!!!a', 'a'),
])
def test_clean_exclamation(input, expected):
    assert clean_exclamation(input) == expected
