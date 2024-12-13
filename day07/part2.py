# https://adventofcode.com/2024/day/7#part2

from __future__ import annotations

import itertools
from dataclasses import dataclass
from typing import Literal

import pytest

import support


@dataclass
class CalibrationEquation:
    test_value: int
    numbers: list[int]


Operator = Literal["+"] | Literal["*"]


def solve(input_data: str) -> int:
    calibration_equations = (
        parse_calibration_equation(line) for line in input_data.splitlines()
    )
    valid_equations = []
    for equation in calibration_equations:
        candidate_operator_seqs = itertools.product(
            ["+", "*", "||"], repeat=len(equation.numbers) - 1
        )
        for operator_seq in candidate_operator_seqs:
            numbers = iter(equation.numbers)
            acc = next(numbers)
            for number, operator in zip(numbers, operator_seq):
                if operator == "+":
                    acc += number
                elif operator == "*":
                    acc *= number
                elif operator == "||":
                    acc = int(str(acc) + str(number))
                else:
                    raise ValueError

                if acc > equation.test_value:
                    break
            if acc == equation.test_value:
                valid_equations.append(equation)
                break

    return sum(equation.test_value for equation in valid_equations)


def parse_calibration_equation(s: str) -> str:
    test_value_s, numbers_s = s.strip().split(":")
    test_value = int(test_value_s)
    numbers = [int(n) for n in numbers_s.strip().split(" ")]
    return CalibrationEquation(test_value, numbers)


EXAMPLE_1 = """\
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
"""
EXPECTED_1 = 11387


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
