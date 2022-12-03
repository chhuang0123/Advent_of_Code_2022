import sys

shape_score = {
    'ROCK': 1,
    'PAPER': 2,
    'SCISSORS': 3,
}

shape_map = {
    'A': 'ROCK',
    'X': 'ROCK',
    'B': 'PAPER',
    'Y': 'PAPER',
    'C': 'SCISSORS',
    'Z': 'SCISSORS',
}


def compare(opponent_shape, my_shape):
    if (
        (opponent_shape == 'ROCK' and my_shape == 'SCISSORS')
        or (opponent_shape == 'PAPER' and my_shape == 'ROCK')
        or (opponent_shape == 'SCISSORS' and my_shape == 'PAPER')
    ):
        return 0
    elif (
        (opponent_shape == 'ROCK' and my_shape == 'ROCK')
        or (opponent_shape == 'PAPER' and my_shape == 'PAPER')
        or (opponent_shape == 'SCISSORS' and my_shape == 'SCISSORS')
    ):
        return 3
    elif (
        (opponent_shape == 'ROCK' and my_shape == 'PAPER')
        or (opponent_shape == 'PAPER' and my_shape == 'SCISSORS')
        or (opponent_shape == 'SCISSORS' and my_shape == 'ROCK')
    ):
        return 6


def get_score(opponent_shape, my_shape):
    return shape_score[shape_map[my_shape]] + compare(
        shape_map[opponent_shape], shape_map[my_shape]
    )


def match_shape(opponent_shape, rule):
    if (
        (rule == 'X' and opponent_shape == 'PAPER')
        or (rule == 'Y' and opponent_shape == 'ROCK')
        or (rule == 'Z' and opponent_shape == 'SCISSORS')
    ):
        return 'ROCK'
    elif (
        (rule == 'X' and opponent_shape == 'SCISSORS')
        or (rule == 'Y' and opponent_shape == 'PAPER')
        or (rule == 'Z' and opponent_shape == 'ROCK')
    ):
        return 'PAPER'
    elif (
        (rule == 'X' and opponent_shape == 'ROCK')
        or (rule == 'Y' and opponent_shape == 'SCISSORS')
        or (rule == 'Z' and opponent_shape == 'PAPER')
    ):
        return 'SCISSORS'


def get_score_2(opponent_shape, my_shape):
    new_shape = match_shape(shape_map[opponent_shape], my_shape)
    return shape_score[new_shape] + compare(shape_map[opponent_shape], new_shape)


if __name__ == '__main__':
    filename = sys.argv[1]

    sum_part_1 = 0
    sum_part_2 = 0
    with open(filename, 'r') as f:
        for line in f.readlines():
            shapes = line.strip().split()
            sum_part_1 += get_score(shapes[0], shapes[1])
            sum_part_2 += get_score_2(shapes[0], shapes[1])

    print(f'part 1: {sum_part_1}')
    print(f'part 2: {sum_part_2}')
