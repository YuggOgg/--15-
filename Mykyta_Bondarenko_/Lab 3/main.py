def Sum(num1, num2):
    if num1 + num2 == 10:
        print(num1, "+", num2)

array = [2, 2, 8, 1, 4, 9, 3, 8, 2]

for i in array:
    for j in array:
        Sum(i, j)
