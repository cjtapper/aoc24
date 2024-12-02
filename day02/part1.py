# https://adventofcode.com/2024/day/2

from __future__ import annotations

import itertools

import pytest

import support

MIN_LEVEL_DIFFERENCE = 1
MAX_LEVEL_DIFFERENCE = 3


def solve(input_data: str) -> int:
    reports = (parse_report(line) for line in input_data.splitlines())

    return sum(is_safe(report) for report in reports)


Report = list[int]


def parse_report(s: str) -> Report:
    return [int(level) for level in s.split()]


def is_safe(report: Report) -> bool:
    differences = [b - a for a, b in itertools.pairwise(report)]
    is_monotonic = all(d < 0 for d in differences) or all(d > 0 for d in differences)
    all_differences_tolerable = all(
        MIN_LEVEL_DIFFERENCE <= abs(d) <= MAX_LEVEL_DIFFERENCE for d in differences
    )
    return is_monotonic and all_differences_tolerable


EXAMPLE_1 = """\
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""
EXPECTED_1 = 2


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
