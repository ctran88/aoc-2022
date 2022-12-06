from collections import deque
import re
from typing import Dict, List, Tuple


def parse_file() -> Tuple[List[str], List[str]]:
    with open("day5_input.txt") as f:
        header: List[str] = []
        while f.readable():
            line = f.readline()
            if line == "\n":
                break

            header.append(line)

        body = [line for line in f.read().splitlines()]
        return header, body


def parse_stacks(header: List[str]) -> Dict[int, deque]:
    stack_columns = header[-1]
    stacks: Dict[int, deque] = {}
    stack_index = []

    for i, char in enumerate(stack_columns):
        if char.isdigit():
            stacks[int(char)] = deque()
            stack_index.append(i)

    for line in header:
        for i, index in enumerate(stack_index):
            char = line[index]
            if char.isalpha():
                stacks[i + 1].insert(0, char)

    return stacks


def parse_crane_directions(body: List[str]) -> List[List[int]]:
    return [
        [int(i) for i in re.split(r"move|from|to", line.replace(" ", ""))[1:]]
        for line in body
    ]


def move_stacks(
    stacks: Dict[int, deque], crane_directions: List[List[int]]
) -> Dict[int, deque]:
    for directions in crane_directions:
        move_count, from_stack, to_stack = directions

        for _ in range(0, move_count):
            item = stacks[from_stack].pop()
            stacks[to_stack].append(item)

    return stacks


def move_stacks_part_2(
    stacks: Dict[int, deque], crane_directions: List[List[int]]
) -> Dict[int, deque]:
    for directions in crane_directions:
        move_count, from_stack, to_stack = directions

        items_to_move = [stacks[from_stack].pop() for _ in range(0, move_count)]
        for _ in range(0, len(items_to_move)):
            stacks[to_stack].append(items_to_move.pop())

    return stacks


def get_top_crates(stacks: Dict[int, deque]) -> str:
    return "".join([stacks[key].pop() for key in stacks.keys()])


if __name__ == "__main__":
    header, body = parse_file()
    stacks = parse_stacks(header)
    crane_directions = parse_crane_directions(body)

    # final_stacks = move_stacks(stacks, crane_directions)
    final_stacks = move_stacks_part_2(stacks, crane_directions)

    top_crates = get_top_crates(final_stacks)
    print(top_crates)
