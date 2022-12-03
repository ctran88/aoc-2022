from typing import List


INPUT_VALUE_MAP = {
    "A": "rock",
    "X": "rock",
    "B": "paper",
    "Y": "paper",
    "C": "scissors",
    "Z": "scissors",
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


def parse_file() -> List[List[str]]:
    with open("day2_input.txt") as f:
        play_pairs = f.read().splitlines()

    return [
        [INPUT_VALUE_MAP[value] for value in pair.split(" ")] for pair in play_pairs
    ]


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


def get_total_score(play_pair_results: List[int]) -> int:
    return sum(play_pair_results)


if __name__ == "__main__":
    play_pairs = parse_file()
    play_pair_results = get_play_pairs_results(play_pairs)
    total_score = get_total_score(play_pair_results)
    print(total_score)
