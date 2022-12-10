import sys


def get_signal_strength(cycle_count, x):
    if cycle_count in [20, 60, 100, 140, 180, 220]:
        return x * cycle_count

    return 0


if __name__ == '__main__':
    filename = sys.argv[1]

    lines = None
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f.readlines()]

    X = 1
    cycle_count = 0
    previous_cycle = ''
    sum_signal_strength = 0

    for line in lines:
        cycles = line.split()

        cycle = cycles.pop(0)
        cycle_count += 1
        sum_signal_strength += get_signal_strength(cycle_count, X)

        if cycle == 'noop':
            pass
        elif cycle == 'addx':
            previous_cycle = cycle

            cycle = cycles.pop(0)
            cycle_count += 1
            sum_signal_strength += get_signal_strength(cycle_count, X)

            X = X + int(cycle)

    print(f'part 1: {sum_signal_strength}')
