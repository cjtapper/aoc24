# https://adventofcode.com/2024/day/3

from __future__ import annotations

import re

import pytest

import support


def solve(input_data: str) -> int:
    pattern = re.compile(r"do\(\)|don't\(\)|mul\((\d+),(\d+)\)")
    program = pattern.finditer(input_data)

    acc = 0
    process_mul = True
    for instruction in program:
        match instruction.group(0):
            case "do()":
                process_mul = True
            case "don't()":
                process_mul = False
            case _ if process_mul:
                a, b = instruction.groups()
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
