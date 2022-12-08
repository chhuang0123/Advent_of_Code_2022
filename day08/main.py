import sys


def check_visible(trees, x, y):
    row_count = len(trees)
    column_count = len(trees[0])

    if x == 0 or y == 0:
        return 1
    elif x == row_count - 1 or y == column_count - 1:
        return 1
    else:
        # check up
        result_up = True
        for i in range(0, x):
            if trees[x][y] <= trees[i][y]:
                result_up = False
                break

        if result_up:
            return 1

        # check down
        result_down = True
        for i in range(x + 1, row_count):
            if trees[x][y] <= trees[i][y]:
                result_down = False
                break

        if result_down:
            return 1

        # check left
        result_left = True
        for j in range(0, y):
            if trees[x][y] <= trees[x][j]:
                result_left = False
                break

        if result_left:
            return 1

        # check right
        result_right = True
        for j in range(y + 1, column_count):
            if trees[x][y] <= trees[x][j]:
                result_right = False
                break

        if result_right:
            return 1

    return 0


def get_scenic_score(trees, x, y):
    row_count = len(trees)
    column_count = len(trees[0])

    # check up
    up_score = 0
    for i in range(x - 1, -1, -1):
        up_score += 1
        if trees[x][y] <= trees[i][y]:
            break

    # check down
    down_score = 0
    for i in range(x + 1, row_count):
        down_score += 1
        if trees[x][y] <= trees[i][y]:
            break

    # check left
    left_score = 0
    for j in range(y - 1, -1, -1):
        left_score += 1
        if trees[x][y] <= trees[x][j]:
            break

    # check right
    right_score = 0
    for j in range(y + 1, column_count):
        right_score += 1
        if trees[x][y] <= trees[x][j]:
            break

    return up_score * down_score * left_score * right_score


if __name__ == '__main__':
    filename = sys.argv[1]

    trees = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            trees.append([int(c) for c in line.strip()])

    total = 0
    max = 0
    for i in range(len(trees)):
        for j in range(len(trees[i])):
            result_1 = check_visible(trees, i, j)
            total += result_1

            result_2 = get_scenic_score(trees, i, j)
            if result_2 > max:
                max = result_2

    print(f'part 1: {total}')
    print(f'part 2: {max}')
