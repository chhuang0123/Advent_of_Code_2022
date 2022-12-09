import sys


class File:
    def __init__(self, name, size, prefix) -> None:
        self.name = name
        self.size = int(size)
        self.prefix = '/' if prefix == '/' else prefix[1:]

    def __str__(self):
        return f'prefix: {self.prefix}, name: {self.name}, size: {self.size}'


if __name__ == '__main__':
    filename = sys.argv[1]

    commands = []
    with open(filename, 'r') as f:
        commands = [str.strip(line).split() for line in f.readlines()]

    levels = []
    files = []
    dirs = {'/': 0}
    for command in commands:
        if command[0] == '$':
            if command[1] == 'cd':
                if command[2] == '..':
                    levels.pop()
                else:
                    levels.append(command[2])
            elif command[1] == 'ls':
                pass
        else:
            if command[0] == 'dir':
                dir_name = ('/'.join(levels) + '/' + command[1])[1:]
                dirs.setdefault(dir_name, 0)
            else:
                prefix = '/'.join(levels)
                files.append(File(command[1], command[0], prefix))

    for f in files:
        for k in dirs.keys():
            if str.startswith(f.prefix, k):
                dirs[k] += f.size

    result = sum([v for v in dirs.values() if v < 100000])
    print(f'part 1: {result}')

    total_space = 70000000
    desired_space = 30000000
    free_space = total_space - dirs['/']
    result = sorted([v for v in dirs.values() if v > (desired_space - free_space)])
    print(f'part 2: {result[0]}')
