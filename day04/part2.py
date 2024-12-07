# https://adventofcode.com/2024/day/4#part2

from __future__ import annotations

import pytest

import support


def solve(input_data: str) -> int:
    word_search = input_data.strip().splitlines()
    left_boundary = 0
    right_boundary = len(word_search[0])
    top_boundary = 0
    bottom_boundary = len(word_search)

    acc = 0
    for x in range(right_boundary):
        for y in range(bottom_boundary):
            if word_search[y][x] != "A":
                continue

            if not (
                y + 1 < bottom_boundary
                and y - 1 >= top_boundary
                and x + 1 < right_boundary
                and x - 1 >= left_boundary
            ):
                continue

            # M.M
            # .A.
            # S.S
            if (
                word_search[y - 1][x - 1] == "M"
                and word_search[y + 1][x + 1] == "S"
                and word_search[y - 1][x + 1] == "M"
                and word_search[y + 1][x - 1] == "S"
            ):
                acc += 1
            # S.S
            # .A.
            # M.M
            if (
                word_search[y + 1][x + 1] == "M"
                and word_search[y - 1][x - 1] == "S"
                and word_search[y + 1][x - 1] == "M"
                and word_search[y - 1][x + 1] == "S"
            ):
                acc += 1
            # S.M
            # .A.
            # S.M
            if (
                word_search[y + 1][x + 1] == "M"
                and word_search[y - 1][x - 1] == "S"
                and word_search[y + 1][x - 1] == "S"
                and word_search[y - 1][x + 1] == "M"
            ):
                acc += 1
            # M.S
            # .A.
            # M.S
            if (
                word_search[y + 1][x + 1] == "S"
                and word_search[y - 1][x - 1] == "M"
                and word_search[y + 1][x - 1] == "M"
                and word_search[y - 1][x + 1] == "S"
            ):
                acc += 1

    return acc


def parse_line(line: str) -> str:
    return line


EXAMPLE_1 = """\
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""
EXPECTED_1 = 9


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
