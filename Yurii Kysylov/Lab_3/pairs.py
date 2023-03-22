def Print(_i, _j):
    print(_i, "+", _j)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in numbers:
    for j in numbers:
        if i + j == 10:
            Print(i, j)