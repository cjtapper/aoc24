# FIXME: https://adventofcode.com/2024/day/x

from __future__ import annotations

import pytest

import support


def solve(input_data: str) -> int:
    values = (parse_line(line) for line in input_data.splitlines())
    for v in values:
        pass

    # TODO: implement solution here!
    return 0


def parse_line(line: str) -> str:
    return line


EXAMPLE_1 = """\

"""
EXPECTED_1 = 0


@pytest.mark.parametrize(
    "input_data,expected",
    [
        (EXAMPLE_1, EXPECTED_1),
    ],
)
def test_solve(input_data, expected):
    assert solve(input_data) == expected


if __name__ == "__main__":
    support.cli(__file__, solve)
