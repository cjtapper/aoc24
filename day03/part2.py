# https://adventofcode.com/2024/day/3

from __future__ import annotations

import re

import pytest

import support


def solve(input_data: str) -> int:
    pattern = re.compile(r"do\(\)|don't\(\)|mul\((\d+),(\d+)\)")
    acc = 0
    do = True
    for match in pattern.finditer(input_data):
        if match.group(0) == "do()":
            do = True
        elif match.group(0) == "don't()":
            do = False
        elif do:
            a, b = match.groups()
            acc += int(a) * int(b)
    return acc


EXAMPLE_1 = """\
xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
"""
EXPECTED_1 = 48


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
