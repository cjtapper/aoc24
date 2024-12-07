# https://adventofcode.com/2024/day/4

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
            if word_search[y][x] != "X":
                continue

            # Check horizontals
            if (
                x + 3 < right_boundary
                and word_search[y][x + 1] == "M"
                and word_search[y][x + 2] == "A"
                and word_search[y][x + 3] == "S"
            ):
                acc += 1
            if (
                x - 3 >= left_boundary
                and word_search[y][x - 1] == "M"
                and word_search[y][x - 2] == "A"
                and word_search[y][x - 3] == "S"
            ):
                acc += 1

            # Check vertical
            if (
                y + 3 < bottom_boundary
                and word_search[y + 1][x] == "M"
                and word_search[y + 2][x] == "A"
                and word_search[y + 3][x] == "S"
            ):
                acc += 1
            if (
                y - 3 >= top_boundary
                and word_search[y - 1][x] == "M"
                and word_search[y - 2][x] == "A"
                and word_search[y - 3][x] == "S"
            ):
                acc += 1

            # check diagonals
            if (
                y + 3 < bottom_boundary
                and x + 3 < right_boundary
                and word_search[y + 1][x + 1] == "M"
                and word_search[y + 2][x + 2] == "A"
                and word_search[y + 3][x + 3] == "S"
            ):
                acc += 1
            if (
                y + 3 < bottom_boundary
                and x - 3 >= left_boundary
                and word_search[y + 1][x - 1] == "M"
                and word_search[y + 2][x - 2] == "A"
                and word_search[y + 3][x - 3] == "S"
            ):
                acc += 1
            if (
                y - 3 >= top_boundary
                and x - 3 >= left_boundary
                and word_search[y - 1][x - 1] == "M"
                and word_search[y - 2][x - 2] == "A"
                and word_search[y - 3][x - 3] == "S"
            ):
                acc += 1
            if (
                y - 3 >= top_boundary
                and x + 3 < right_boundary
                and word_search[y - 1][x + 1] == "M"
                and word_search[y - 2][x + 2] == "A"
                and word_search[y - 3][x + 3] == "S"
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
EXPECTED_1 = 18


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
