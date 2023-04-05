a, countl_z, count_and = False, 0, 0

while a != True:
    file = open(input('Enter puth to file: '), 'r')
    count_lines = file.readlines()
    empty_lines = [line for line in count_lines if line == '\n']
    z_lines = [line for line in count_lines if 'z' in line]
    count_z = len(z_lines)
    count_z_lines = [line for line in count_lines for z in line if z == 'z']
    and_lines = [line for line in count_lines]
    for line in and_lines:
        if 'and' in line: count_and += 1
    print(f'total lines: {len(count_lines)}\nempty lines: {len(empty_lines)}\n')
    print(f'lines with "z": {count_z}\n')
    print(f'"z" count": {len(count_z_lines)}\nlines with "and": {count_and}\n')

    key = str(input('Exit(x) | Analize new file(f)\nEnter char:'))
    a = True if key == 'x' else False if key == 'y' else True

