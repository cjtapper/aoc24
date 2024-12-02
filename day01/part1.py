# https://adventofcode.com/2024/day/1

from __future__ import annotations

import pytest

import support


def solve(input_data: str) -> int:
    left_numbers = []
    right_numbers = []
    for line in input_data.splitlines():
        left, right = parse_line(line)
        left_numbers.append(left)
        right_numbers.append(right)

    left_numbers.sort()
    right_numbers.sort()

    return sum(
        distance(left, right) for left, right in zip(left_numbers, right_numbers)
    )


def parse_line(line: str) -> tuple[int, int]:
    left, right = line.split()
    return int(left), int(right)


def distance(a: int, b: int) -> int:
    return abs(a - b)


EXAMPLE_1 = """\
3   4
4   3
2   5
1   3
3   9
3   3
"""
EXPECTED_1 = 11


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
