# https://adventofcode.com/2024/day/1#part2

from __future__ import annotations

from collections import Counter

import pytest

import support


def solve_for(input_data: str) -> int:
    left_numbers: list[int] = []
    right_numbers = Counter[int]()
    for line in input_data.splitlines():
        left, right = parse_line(line)
        left_numbers.append(left)
        right_numbers[right] += 1

    return sum(left * right_numbers[left] for left in left_numbers)


def parse_line(line: str) -> tuple[int, int]:
    left, right = line.split()
    return int(left), int(right)


EXAMPLE_1 = """\
3   4
4   3
2   5
1   3
3   9
3   3
"""
EXPECTED_1 = 31


@pytest.mark.parametrize(
    "input_data,expected",
    [
        (EXAMPLE_1, EXPECTED_1),
    ],
)
def test_example(input_data, expected):
    assert solve_for(input_data) == expected


if __name__ == "__main__":
    support.cli(__file__, solve_for)
