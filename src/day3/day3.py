from functools import reduce
from typing import List


LOWERCASE_A_ASCII_DECIMAL = 97
UPPERCASE_A_ASCII_DECIMAL = 65


def parse_file(rucksacks_in_group: int) -> List[List[str]]:
    with open("day3_input.txt") as f:
        lines = f.read().splitlines()

    return (
        [
            lines[i : i + rucksacks_in_group]
            for i in range(0, len(lines), rucksacks_in_group)
        ]
        if rucksacks_in_group > 1
        else [[line[: len(line) // 2], line[len(line) // 2 :]] for line in lines]
    )


def get_priorities(rucksack_compartments: List[List[str]]):
    return [
        _get_priority(_get_intersection(*compartments))
        for compartments in rucksack_compartments
    ]


def get_total_score(priorities: List[int]) -> int:
    return sum(priorities)


def _get_intersection(*args: str) -> str:
    compartments = [set(compartment) for compartment in args]
    intersection = reduce(set.intersection, compartments)
    return intersection.pop()


def _get_priority(letter: str) -> int:
    return (
        ord(letter) - LOWERCASE_A_ASCII_DECIMAL + 1
        if letter.islower()
        else ord(letter) - UPPERCASE_A_ASCII_DECIMAL + 27
    )


if __name__ == "__main__":
    rucksack_compartments = parse_file(1)
    priorities = get_priorities(rucksack_compartments)
    total_priority_score = get_total_score(priorities)
    print(total_priority_score)

    rucksack_compartments = parse_file(3)
    priorities = get_priorities(rucksack_compartments)
    total_priority_score = get_total_score(priorities)
    print(total_priority_score)
