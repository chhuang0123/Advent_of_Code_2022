import sys


def convert_range(range_char):
    return list(map(int, range_char.split('-')))


def is_fully_overlapped(range1, range2):
    length_range1 = range1[1] - range1[0]
    length_range2 = range2[1] - range2[0]

    if length_range1 >= length_range2:
        return range1[0] <= range2[0] and range1[1] >= range2[1]

    return range2[0] <= range1[0] and range2[1] >= range1[1]


def is_overlapped(range1, range2):
    return range2[1] >= range1[0] and range1[1] >= range2[0]


if __name__ == '__main__':
    filename = sys.argv[1]

    sum_part_1 = 0
    sum_part_2 = 0
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines:
            range_char = line.strip().split(',')
            range_start_end_1 = convert_range(range_char[0])
            range_start_end_2 = convert_range(range_char[1])

            if is_fully_overlapped(range_start_end_1, range_start_end_2):
                sum_part_1 += 1

            if is_overlapped(range_start_end_1, range_start_end_2):
                sum_part_2 += 1

    print(f'part 1: {sum_part_1}')
    print(f'part 2: {sum_part_2}')
