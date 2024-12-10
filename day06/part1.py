# https://adventofcode.com/2024/day/6

from __future__ import annotations

from dataclasses import dataclass

import pytest

import support

GUARD = "^"


@dataclass(frozen=True)
class Position:
    x: int
    y: int

    def __add__(self, other):
        if isinstance(other, Vector):
            return Position(self.x + other.x, self.y + other.y)

        return super().__add__(other)


@dataclass
class Vector:
    x: int
    y: int

    def turn_right(self):
        return Vector(-self.y, self.x)


def solve(input_data: str) -> int:
    map = input_data.strip().splitlines()

    position = find_guard(map)
    direction = Vector(0, -1)
    seen = set()

    while True:
        seen.add(position)
        next_position = position + direction

        if not (0 <= next_position.x < len(map[0]) and 0 <= next_position.y < len(map)):
            break

        if map[next_position.y][next_position.x] == "#":
            direction = direction.turn_right()
        else:
            position = next_position

    return len(seen)


def find_guard(map: list[str]) -> Position:
    for y, row in enumerate(map):
        x = row.find(GUARD)
        if x == -1:
            continue
        return Position(x, y)


def parse_line(line: str) -> str:
    return line


EXAMPLE_1 = """\
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""
EXPECTED_1 = 41


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
