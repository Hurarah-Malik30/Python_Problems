import random

matrix_4 = [[random.random() for _ in range(4)]for _ in range(4)]
# print(matrix_4)

diaginal_list = []

for i in range(4):
    for j in range(4):
        if i == j:
            diaginal_list.append(matrix_4[i][j])

print(diaginal_list)