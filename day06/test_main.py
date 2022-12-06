import sys

import pytest


def check_start_packet(marker, max_length=4):
    for i in range(len(marker) - 4):
        packet = set(marker[i : i + max_length])
        if len(packet) == max_length:
            return i + max_length

    return -1


@pytest.mark.parametrize(
    "marker,expected",
    [
        ('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 7),
        ('bvwbjplbgvbhsrlpgdmjqwftvncz', 5),
        ('nppdvjthqldpwncqszvftbrmjlhg', 6),
        ('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 10),
        ('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 11),
    ],
)
def test_check_start_packet(marker, expected):
    actual = check_start_packet(marker)
    assert actual == expected


if __name__ == '__main__':
    filename = sys.argv[1]

    with open(filename, 'r') as f:
        line = f.readline()
        result = check_start_packet(line)
        print(f"part 1: {result}")
