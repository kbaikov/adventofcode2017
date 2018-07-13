import pytest

from advent2017_4 import no_anagrams, no_duplicates


@pytest.mark.parametrize(
    "input, expected",
    [
        ("abcde fghij", True),
        ("abcde xyz ecdab", False),
        ("a ab abc abd abf abj", True),
        ("iiii oiii ooii oooi oooo", True),
        ("oiii ioii iioi iiio", False),
    ],
)
def test_no_anagrams(input, expected):
    assert no_anagrams(input) == expected


@pytest.mark.parametrize(
    "input, expected",
    [("aa bb cc dd ee", True), ("aa bb cc dd aa", False), ("aa bb cc dd aaa", True)],
)
def test_no_duplicates(input, expected):
    assert no_duplicates(input) == expected
