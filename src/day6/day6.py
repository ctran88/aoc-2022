def parse_file() -> str:
    with open("day6_input.txt") as f:
        line = f.readline()
    return line


def get_start_of_packet_marker(message: str, unique_character_count: int) -> int:
    start_of_packet_marker = 0
    for i in range(len(message)):
        end_range = i + unique_character_count
        set_of_chars = set(message[i:end_range])
        if len(set_of_chars) == unique_character_count:
            start_of_packet_marker = end_range
            break

    return start_of_packet_marker


if __name__ == "__main__":
    message = parse_file()
    start_of_packet_marker = get_start_of_packet_marker(message, 4)
    print(start_of_packet_marker)

    start_of_packet_marker = get_start_of_packet_marker(message, 14)
    print(start_of_packet_marker)