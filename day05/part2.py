# https://adventofcode.com/2024/day/5

from __future__ import annotations

import pytest

import support


def solve(input_data: str) -> int:
    rules_section, updates_section = input_data.strip().split("\n\n")
    rules = [parse_rule(line) for line in rules_section.splitlines()]
    updates = [parse_update(line) for line in updates_section.splitlines()]

    acc = 0
    for update in updates:
        if check_rules(update, rules):
            continue
        else:
            update = sort_by_rules(update, rules)
            middle_page = update[len(update) // 2]
            acc += middle_page
    return acc


def sort_by_rules(update, rules):
    update = update.copy()
    recheck = True
    while recheck:
        recheck = False
        for rule in rules:
            before = rule["before"]
            after = rule["after"]

            if before not in update or after not in update:
                continue

            if update.index(before) > update.index(after):
                update[update.index(before)], update[update.index(after)] = (
                    update[update.index(after)],
                    update[update.index(before)],
                )
                recheck = True

    return update


def check_rules(update: list, rules):
    for rule in rules:
        before = rule["before"]
        after = rule["after"]

        if before not in update or after not in update:
            continue

        if update.index(before) > update.index(after):
            return False
    return True


def parse_rule(line: str) -> str:
    before, after = line.split("|")
    return {"before": int(before), "after": int(after)}


def parse_update(line: str) -> list:
    return [int(page) for page in line.split(",")]


EXAMPLE_1 = """\
7|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""
EXPECTED_1 = 123


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
