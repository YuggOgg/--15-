while True:
    file = open(input('Введіть шлях до файлу: '), 'r')
    count_lines = file.readlines()
    empty_lines = [line for line in count_lines if line == '\n']
    z_lines = [line for line in count_lines if 'z' in line]
    count_z = len(z_lines)
    count_z_lines = [line for line in count_lines for z in line if z == 'z']
    and_lines = [line for line in count_lines]
    count_and = sum('and' in line for line in and_lines)
    print(f'Всього рядків: {len(count_lines)}\nпорожніх рядків: {len(empty_lines)}')
    print(f'Рядків з "z": {count_z}')
    print(f'Кількість "z": {len(count_z_lines)}\nРядків з "and": {count_and}')

    key = str(input('Вийти (x) | Проаналізувати новий файл (f)\nВведіть символ: '))
    if key == 'x': break
