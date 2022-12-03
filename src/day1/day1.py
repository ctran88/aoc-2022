from typing import List


def parse_file() -> List[List[int]]:
    with open("day1_input.txt") as f:
        item_groups = f.read().split("\n\n")

    item_group_list = [i.split("\n") for i in item_groups]
    return [[int(i) for i in group if i.isdigit()] for group in item_group_list]


def sum_item_groups(item_group_list: List[List[int]]) -> List[int]:
    return [sum(group) for group in item_group_list]


def get_max_item_group(summed_item_group_list: List[int]) -> int:
    return max(summed_item_group_list)


def get_top_three_item_groups(summed_item_group_list: List[int]) -> int:
    summed_item_group_list.sort(reverse=True)
    return sum(summed_item_group_list[:3])


if __name__ == "__main__":
    item_group_list = parse_file()
    summed_item_group_list = sum_item_groups(item_group_list)
    max_item_group = get_max_item_group(summed_item_group_list)
    print(max_item_group)

    top_three_item_groups = get_top_three_item_groups(summed_item_group_list)
    print(top_three_item_groups)
