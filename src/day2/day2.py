from typing import Dict, List


INPUT_VALUE_MAP = {
    "A": "rock",
    "X": "rock",
    "B": "paper",
    "Y": "paper",
    "C": "scissors",
    "Z": "scissors",
}
INPUT_VALUE_MAP_PART_2 = {
    "A": "rock",
    "X": "lose",
    "B": "paper",
    "Y": "draw",
    "C": "scissors",
    "Z": "win",
}
PLAY_ADVANTAGE_MAP = {"rock": "paper", "paper": "scissors", "scissors": "rock"}

CHOICE_SCORE_MAP = {
    "rock": 1,
    "paper": 2,
    "scissors": 3,
}
MATCH_SCORE_MAP = {
    "lose": 0,
    "draw": 3,
    "win": 6,
}


def parse_file(input_mapper: Dict[str, str]) -> List[List[str]]:
    with open("day2_input.txt") as f:
        play_pairs = f.read().splitlines()

    return [[input_mapper[value] for value in pair.split(" ")] for pair in play_pairs]


def get_play_pairs_results(play_pairs: List[List[str]]) -> List[int]:
    play_pair_results = []

    for them, us in play_pairs:
        score = CHOICE_SCORE_MAP[us]

        if us == PLAY_ADVANTAGE_MAP[them]:
            score += MATCH_SCORE_MAP["win"]
        elif us == them:
            score += MATCH_SCORE_MAP["draw"]
        else:
            score += MATCH_SCORE_MAP["lose"]

        play_pair_results.append(score)

    return play_pair_results


def get_play_pairs_results_part_2(play_pairs: List[List[str]]) -> List[int]:
    return [
        MATCH_SCORE_MAP[how_to_play] + CHOICE_SCORE_MAP[get_choice(them, how_to_play)]
        for them, how_to_play in play_pairs
    ]


def get_choice(their_choice: str, how_to_play: str) -> str:
    if how_to_play == "win":
        choice = PLAY_ADVANTAGE_MAP[their_choice]
    elif how_to_play == "draw":
        choice = their_choice
    else:
        choice = [
            key
            for key in CHOICE_SCORE_MAP.keys()
            if key not in [PLAY_ADVANTAGE_MAP[their_choice], their_choice]
        ][0]

    return choice


def get_total_score(play_pair_results: List[int]) -> int:
    return sum(play_pair_results)


if __name__ == "__main__":
    play_pairs = parse_file(INPUT_VALUE_MAP)
    play_pair_results = get_play_pairs_results(play_pairs)
    total_score = get_total_score(play_pair_results)
    print(total_score)

    play_pairs = parse_file(INPUT_VALUE_MAP_PART_2)
    play_pair_results_part2 = get_play_pairs_results_part_2(play_pairs)
    total_score = get_total_score(play_pair_results_part2)
    print(total_score)
