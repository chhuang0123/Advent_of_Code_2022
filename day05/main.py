import sys

if __name__ == '__main__':
    filename = sys.argv[1]

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
        stacks = dict()
        nums = lines[stop_index - 1].strip().split('   ')
        for num in nums:
            num_index = lines[stop_index - 1].index(num)
            tmp_chars = list()
            for line in lines[0 : stop_index - 1]:
                if num_index > len(line):
                    continue

                if line[num_index] != ' ':
                    tmp_chars.insert(0, line[num_index])

            stacks[num] = tmp_chars

        # part 1 - procedures
        for line in lines[stop_index + 1 :]:
            data = line.split()
            move_count, from_index, to_index = int(data[1]), data[3], data[5]

            for i in range(move_count):
                tmp_char = stacks[from_index].pop()
                stacks[to_index].append(tmp_char)

        result = []
        for num in nums:
            result.append(stacks[num].pop())

        print(f"part 1: {''.join(result)}")
