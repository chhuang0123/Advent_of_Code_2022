import sys

if __name__ == '__main__':
    filename = sys.argv[1]

    sum_list = list()
    with open(filename, 'r') as f:
        lines = f.read().split('\n\n')
        for line in lines:
            sum_value = sum(map(int, line.strip().split()))
            sum_list.append(sum_value)

    sum_list.sort(reverse=True)

    print(f'part 1: {sum_list[0]}')
    print(f'part 2: {sum(sum_list[0:3])}')
