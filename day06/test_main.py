import sys

import pytest


def check_start_packet(marker, max_length=4):
    for i in range(len(marker) - max_length):
        packet = set(marker[i : i + max_length])
        if len(packet) == max_length:
            return i + max_length

    return -1


@pytest.mark.parametrize(
    "marker,expected,max_length",
    [
        ('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 7, 4),
        ('bvwbjplbgvbhsrlpgdmjqwftvncz', 5, 4),
        ('nppdvjthqldpwncqszvftbrmjlhg', 6, 4),
        ('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 10, 4),
        ('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 11, 4),
        ('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 19, 14),
        ('bvwbjplbgvbhsrlpgdmjqwftvncz', 23, 14),
        ('nppdvjthqldpwncqszvftbrmjlhg', 23, 14),
        ('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 29, 14),
        ('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 26, 14),
    ],
)
def test_check_start_packet(marker, expected, max_length):
    actual = check_start_packet(marker, max_length)
    assert actual == expected


if __name__ == '__main__':
    filename = sys.argv[1]

    with open(filename, 'r') as f:
        line = f.readline()
        result = check_start_packet(line)
        print(f"part 1: {result}")

        result = check_start_packet(line, 14)
        print(f"part 2: {result}")
