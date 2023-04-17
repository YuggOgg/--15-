def FindPairSum(number, numbers):
 for i in numbers:
    for j in numbers:
        if (i + j == number) & (i != j):
            print(f"{i} + {j} = 10")
            
arr_num = [1, 2, 3, 4, 5, 6, 7]

FindPairSum(10, arr_num)