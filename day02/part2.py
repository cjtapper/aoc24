# https://adventofcode.com/2024/day/2#part2

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


def is_safe(report: Report, *, recurse=True) -> bool:
    sub_reports = []
    for i in range(len(report)):
        sub_report = report.copy()
        sub_report.pop(i)

        sub_reports.append(sub_is_safe(sub_report))

    return any(sub_reports)


def sub_is_safe(report):
    last_sign = None
    for a, b in itertools.pairwise(report):
        diff = b - a
        next_sign = sign(diff)
        if last_sign is not None and (next_sign != last_sign or next_sign == 0):
            return False
        last_sign = next_sign
        if not MIN_LEVEL_DIFFERENCE <= abs(diff) <= MAX_LEVEL_DIFFERENCE:
            return False

    return True



def sign(value: int) -> int:
    return value / abs(value) if value else 0


EXAMPLE_1 = """\
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""
EXPECTED_1 = 4

EXAMPLE_2 = """\
8 9 8 7 6
"""
# Would be safe if the first value was removed
EXPECTED_2 = 1


@pytest.mark.parametrize(
    "input_data,expected",
    [
        (EXAMPLE_1, EXPECTED_1),
        (EXAMPLE_2, EXPECTED_2),
    ],
)
def test_solve(input_data, expected):
    assert solve(input_data) == expected


if __name__ == "__main__":
    support.cli(__file__, solve)
