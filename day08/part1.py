# https://adventofcode.com/2024/day/8
from __future__ import annotations

import itertools
from collections import defaultdict

import pytest

import support


def solve(input_data: str) -> int:
    antenna_locations = parse_antenna_locations(input_data.strip())
    map_height = len(input_data.strip().splitlines())
    map_width = len(input_data.strip().splitlines()[0])

    antinode_locations = set()
    for locations in antenna_locations.values():
        for location_a, location_b in itertools.permutations(locations, 2):
            x_distance = location_b[0] - location_a[0]
            y_distance = location_b[1] - location_a[1]

            antinode_a = location_a[0] - x_distance, location_a[1] - y_distance
            antinode_b = location_b[0] + x_distance, location_b[1] + y_distance

            if 0 <= antinode_a[0] < map_width and 0 <= antinode_a[1] < map_height:
                antinode_locations.add(antinode_a)
            if 0 <= antinode_b[0] < map_width and 0 <= antinode_b[1] < map_height:
                antinode_locations.add(antinode_b)

    return len(antinode_locations)


Point = tuple[int, int]


def parse_antenna_locations(s: str) -> dict[str, list[Point]]:
    antenna_locations = defaultdict(list)
    rows = s.splitlines()
    for y, row in enumerate(rows):
        for x, value in enumerate(row):
            if value.isalnum():
                antenna_locations[value].append((x, y))
    return antenna_locations


EXAMPLE_1 = """\
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
"""
EXPECTED_1 = 14


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
