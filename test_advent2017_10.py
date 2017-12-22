import pytest

from advent2017_10 import main


@pytest.mark.parametrize("input, expected", [
    ('aaa!ddd!!cc', 'aaaddcc'),
    ('!!!!a', 'a'),
])
def test_clean_exclamation(input, expected):
    assert clean_exclamation(input) == expected


@pytest.mark.parametrize("input, expected", [
    ('a<>a', 'aa'),
    ('a<asdf>a', 'aa'),
    ('a<<<<>a', 'aa'),
    ('<>', ''),
])
def test_clean_garbage(input, expected):
    assert clean_garbage(input) == expected


@pytest.mark.parametrize("input, expected", [
    ('{}', 1),
    ('{{{}}}', 6),
    ('{{},{}}', 5),
    ('{{{},{},{{}}}}', 16),
    ('{{<ab>},{<ab>},{<ab>},{<ab>}}', 9),
])
def test_score_group(input, expected):
    assert score_group(input) == expected
