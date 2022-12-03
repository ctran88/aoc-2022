from typing import List


LOWERCASE_A_ASCII_DECIMAL = 97
UPPERCASE_A_ASCII_DECIMAL = 65


def parse_file() -> List[List[str]]:
    with open("day3_input.txt") as f:
        rucksacks = f.read().splitlines()

    return [
        [rucksack[: len(rucksack) // 2], rucksack[len(rucksack) // 2 :]]
        for rucksack in rucksacks
    ]


def get_priorities(rucksack_compartments: List[List[str]]):
    return [
        _get_priority(_get_intersection(first_compartment, second_compartment))
        for first_compartment, second_compartment in rucksack_compartments
    ]


def get_total_score(priorities: List[int]) -> int:
    return sum(priorities)


def _get_intersection(first_compartment: str, second_compartment: str) -> str:
    intersection = set(first_compartment) & set(second_compartment)
    return intersection.pop()


def _get_priority(letter: str) -> int:
    return (
        ord(letter) - LOWERCASE_A_ASCII_DECIMAL + 1
        if letter.islower()
        else ord(letter) - UPPERCASE_A_ASCII_DECIMAL + 27
    )


if __name__ == "__main__":
    rucksack_compartments = parse_file()
    priorities = get_priorities(rucksack_compartments)
    total_priority_score = get_total_score(priorities)
    print(total_priority_score)
