def parse_file() -> str:
    with open("day6_input.txt") as f:
        line = f.readline()
    return line


def get_start_of_packet_marker(message: str) -> int:
    start_of_packet_marker = 0
    for i in range(len(message)):
        end_range = i + 4
        set_of_chars = set(message[i:end_range])
        if len(set_of_chars) == 4:
            start_of_packet_marker = end_range
            break

    return start_of_packet_marker


if __name__ == "__main__":
    message = parse_file()
    start_of_packet_marker = get_start_of_packet_marker(message)
    print(start_of_packet_marker)
