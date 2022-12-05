import copy
import sys


def solution_1(stacks, procedures):
    for procedure in procedures:
        move_count, from_index, to_index = procedure[0], procedure[1], procedure[2]

        for _ in range(move_count):
            tmp_char = stacks[from_index].pop()
            stacks[to_index].append(tmp_char)

    result = []
    for num in nums:
        result.append(stacks[num].pop())

    print(f"part 1: {''.join(result)}")


def solution_2(stacks, procedures):
    for procedure in procedures:
        move_count, from_index, to_index = procedure[0], procedure[1], procedure[2]
        pop_index = len(stacks[from_index]) - move_count

        for _ in range(move_count):
            tmp_char = stacks[from_index].pop(pop_index)
            stacks[to_index].append(tmp_char)

    result = []
    for num in nums:
        result.append(stacks[num].pop())

    print(f"part 2: {''.join(result)}")


if __name__ == '__main__':
    filename = sys.argv[1]

    stacks = {}
    procedures = []
    with open(filename, 'r') as f:
        lines = [x.rstrip() for x in f.readlines()]

        # find stack and procedure
        stop_index = 0
        stack_count = -1
        for i in range(len(lines)):
            if lines[i] == '':
                stop_index = i
                stack_count += 1
                break

        # create stacks
        nums = lines[stop_index - 1].strip().split('   ')
        for num in nums:
            num_index = lines[stop_index - 1].index(num)
            tmp_chars = list()
            for line in lines[0 : stop_index - 1]:
                if num_index > len(line):
                    continue

                if line[num_index] != ' ':
                    tmp_chars.insert(0, line[num_index])

            stacks[num] = tmp_chars.copy()

        # create procedures
        for line in lines[stop_index + 1 :]:
            data = line.split()
            procedures.append([int(data[1]), data[3], data[5]])

    stacks_2 = copy.deepcopy(stacks)
    solution_1(stacks, procedures)
    solution_2(stacks_2, procedures)
