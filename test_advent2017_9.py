import pytest

from advent2017_9 import main


@pytest.fixture
def reg():
    return {'registers': {'a': 5}}


def pytest_namespace():
    return {'registers': {'a': 5}}


@pytest.mark.parametrize("input, expected", [
    (('a', '>', 1), True),
    (('a', '<', 1), False),
])
def test_condition(input, expected, monkeypatch):
    registers = {'a': 5}
    # monkeypatch.setattr(registers, "a", 5)
    # registers = pytest.registers
    assert condition(*input) == expected
