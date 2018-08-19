import pytest

from advent2017_18 import process


@pytest.mark.parametrize(
    "input, expected",
    [
        (
            ([("set", "i", "31")], {"i": 0, "pointer": 0, "result": 0}),
            ([("set", "i", "31")], {"i": 31, "pointer": 1, "result": 0}),
        ),
        (
            ([("set", "i", "a")], {"a": 57, "i": 0, "pointer": 0, "result": 0}),
            ([("set", "i", "a")], {"a": 57, "i": 57, "pointer": 1, "result": 0}),
        ),
        (
            ([("add", "i", "31")], {"i": 2, "pointer": 0, "result": 0}),
            ([("add", "i", "31")], {"i": 33, "pointer": 1, "result": 0}),
        ),
        (
            ([("add", "i", "a")], {"a": 2, "i": 3, "pointer": 0, "result": 0}),
            ([("add", "i", "a")], {"a": 2, "i": 5, "pointer": 1, "result": 0}),
        ),
        (
            ([("mul", "i", "31")], {"i": 2, "pointer": 0, "result": 0}),
            ([("mul", "i", "31")], {"i": 62, "pointer": 1, "result": 0}),
        ),
        (
            ([("mul", "i", "a")], {"a": 2, "i": 2, "pointer": 0, "result": 0}),
            ([("mul", "i", "a")], {"a": 2, "i": 4, "pointer": 1, "result": 0}),
        ),
        (
            ([("mod", "i", "10")], {"i": 31, "pointer": 0, "result": 0}),
            ([("mod", "i", "10")], {"i": 1, "pointer": 1, "result": 0}),
        ),
        (
            ([("mod", "i", "a")], {"a": 10, "i": 31, "pointer": 0, "result": 0}),
            ([("mod", "i", "a")], {"a": 10, "i": 1, "pointer": 1, "result": 0}),
        ),
        (
            ([("snd", "i")], {"a": 10, "i": 31, "pointer": 0, "result": 0}),
            ([("snd", "i")], {"a": 10, "i": 31, "pointer": 1, "result": 31}),
        ),
        (
            ([("jgz", "i", "10")], {"i": 0, "pointer": 0, "result": 0}),
            ([("jgz", "i", "10")], {"i": 0, "pointer": 1, "result": 0}),
        ),
        (
            ([("jgz", "i", "10")], {"i": 1, "pointer": 0, "result": 0}),
            ([("jgz", "i", "10")], {"i": 1, "pointer": 10, "result": 0}),
        ),
        (
            ([("jgz", "i", "a")], {"a": 10, "i": 1, "pointer": 0, "result": 0}),
            ([("jgz", "i", "a")], {"a": 10, "i": 1, "pointer": 10, "result": 0}),
        ),
        (
            ([("jgz", "i", "a")], {"a": -5, "i": 1, "pointer": 0, "result": 0}),
            ([("jgz", "i", "a")], {"a": -5, "i": 1, "pointer": -5, "result": 0}),
        ),
        (
            (
                [("rcv", "i")],
                {"a": 10, "i": 1, "pointer": 0, "result": 0, "end_program": None},
            ),
            (
                [("rcv", "i")],
                {"a": 10, "i": 1, "pointer": 0, "result": 0, "end_program": True},
            ),
        ),
        (
            (
                [("rcv", "i")],
                {"a": 10, "i": 0, "pointer": 0, "result": 0, "end_program": None},
            ),
            (
                [("rcv", "i")],
                {"a": 10, "i": 0, "pointer": 1, "result": 0, "end_program": None},
            ),
        ),
    ],
)
def test_process(input, expected):
    assert process(*input) == expected
