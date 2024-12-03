# https://adventofcode.com/2024/day/3

from __future__ import annotations

import re

import pytest

import support


def solve(input_data: str) -> int:
    pattern = re.compile(r"mul\((\d+),(\d+)\)")
    acc = 0
    for match in pattern.finditer(input_data):
        a, b = match.groups()
        acc += int(a) * int(b)
    return acc


EXAMPLE_1 = """\
xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
"""
EXPECTED_1 = 161


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
