import pytest

from advent2017_8 import condition, action


@pytest.mark.parametrize(
    "input, expected",
    [(("a", ">", 1, {"a": 5}), True), (("a", "<", 1, {"a": 5}), False)],
)
def test_condition(input, expected, monkeypatch):
    assert condition(*input) == expected


@pytest.mark.parametrize(
    "input, expected",
    [(("a", "inc", 1, {"a": 5}), {"a": 6}), (("a", "dec", 1, {"a": 5}), {"a": 4})],
)
def test_action(input, expected, monkeypatch):
    assert action(*input) == expected
