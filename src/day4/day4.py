from typing import List, Set


def parse_file() -> List[List[str]]:
    with open("day4_input.txt") as f:
        lines = f.read().splitlines()

    return [line.split(",") for line in lines]


def get_subsets(assignment_pairs: List[List[str]]) -> List[List[Set[int]]]:
    subsets = []

    for pair in assignment_pairs:
        first, second = pair

        first_split = first.split("-")
        second_split = second.split("-")

        first_set = set(range(int(first_split[0]), int(first_split[1]) + 1))
        second_set = set(range(int(second_split[0]), int(second_split[1]) + 1))

        is_subset = first_set.issubset(second_set) or second_set.issubset(first_set)
        if is_subset:
            subsets.append([first_set, second_set])

    return subsets


if __name__ == "__main__":
    assignment_pairs = parse_file()
    subsets = get_subsets(assignment_pairs)
    subset_count = len(subsets)
    print(subset_count)
