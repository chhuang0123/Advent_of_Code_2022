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

        # check_down
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


if __name__ == '__main__':
    filename = sys.argv[1]

    trees = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            trees.append([int(c) for c in line.strip()])

    result = 0
    for i in range(len(trees)):
        for j in range(len(trees[i])):
            result += check_visible(trees, i, j)

    print(f"part 1: {result}")


