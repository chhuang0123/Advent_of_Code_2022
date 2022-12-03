import sys

CODES = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


def find_redundant(compartments):
    half = int(len(compartments) / 2)
    for i in range(half):
        if compartments[i] in compartments[half:]:
            return compartments[i]

    return ''


def find_redundant_of_groups(groups):
    unique_char = set(groups[0])
    for c in unique_char:
        if c in groups[1] and c in groups[2]:
            return c

    return ''


if __name__ == '__main__':
    filename = sys.argv[1]

    sum_part_1 = 0
    sum_part_2 = 0
    with open(filename, 'r') as f:
        lines = f.readlines()

        for line in lines:
            item = find_redundant(line.strip())
            sum_part_1 += CODES.find(item) + 1

        for i in range(int(len(lines) / 3)):
            item = find_redundant_of_groups(
                [
                    lines[3 * i].strip(),
                    lines[3 * i + 1].strip(),
                    lines[3 * i + 2].strip(),
                ]
            )
            sum_part_2 += CODES.find(item) + 1

    print(f'part 1: {sum_part_1}')
    print(f'part 2: {sum_part_2}')
