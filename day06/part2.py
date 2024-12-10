# https://adventofcode.com/2024/day/6#part2
from __future__ import annotations

from copy import deepcopy
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


@dataclass(frozen=True)
class Vector:
    x: int
    y: int

    def turn_right(self):
        return Vector(-self.y, self.x)


def solve(input_data: str) -> int:
    map = [list(row) for row in input_data.strip().splitlines()]

    position = position = find_guard(map)
    direction = direction = Vector(0, -1)
    seen = set()

    new_obstruction_positions = set()
    while True:
        seen.add(position)
        next_position = position + direction

        if not (0 <= next_position.x < len(map[0]) and 0 <= next_position.y < len(map)):
            break

        if next_position not in new_obstruction_positions and next_position not in seen:
            new_map = deepcopy(map)
            new_map[next_position.y][next_position.x] = "#"
            if has_loop(
                new_map,
                start_position=position,
                start_direction=direction,
            ):
                new_obstruction_positions.add(next_position)

        if map[next_position.y][next_position.x] == "#":
            direction = direction.turn_right()
        else:
            position = next_position

    return len(new_obstruction_positions)


def find_guard(map: list[str]) -> Position:
    for y, row in enumerate(map):
        try:
            x = row.index(GUARD)
        except ValueError:
            continue
        return Position(x, y)


def has_loop(map, start_position, start_direction):
    seen: set[tuple[Position, Vector]] = set()
    position = start_position
    direction = start_direction

    while True:
        if (position, direction) in seen:
            return True
        seen.add((position, direction))
        next_position = position + direction

        if not (0 <= next_position.x < len(map[0]) and 0 <= next_position.y < len(map)):
            break

        if map[next_position.y][next_position.x] == "#":
            direction = direction.turn_right()
        else:
            position = next_position

    return False


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
EXPECTED_1 = 6


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
