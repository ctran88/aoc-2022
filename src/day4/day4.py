from typing import List, Set


def parse_file() -> List[List[str]]:
    with open("day4_input.txt") as f:
        lines = f.read().splitlines()

    return [line.split(",") for line in lines]


def get_assignment_sets(assignment_pairs: List[List[str]]) -> List[List[Set[int]]]:
    sets = []

    for pair in assignment_pairs:
        first, second = pair

        first_split = first.split("-")
        second_split = second.split("-")

        first_set = set(range(int(first_split[0]), int(first_split[1]) + 1))
        second_set = set(range(int(second_split[0]), int(second_split[1]) + 1))

        sets.append([first_set, second_set])

    return sets


def get_subset_count(assignment_sets: List[List[Set[int]]]) -> int:
    return len([assignments for assignments in assignment_sets if assignments[0].issubset(assignments[1]) or assignments[1].issubset(assignments[0])])


def get_intersection_count(assignment_sets: List[List[Set[int]]]) -> int:
    return len([assignments for assignments in assignment_sets if len(assignments[0].intersection(assignments[1]))])

if __name__ == "__main__":
    assignment_pairs = parse_file()
    assignment_sets = get_assignment_sets(assignment_pairs)
    subset_count = get_subset_count(assignment_sets)
    print(subset_count)

    intersection_count = get_intersection_count(assignment_sets)
    print(intersection_count)
