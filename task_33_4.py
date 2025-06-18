import random
matrix_column = [[random.random() for _ in range(4)] for _ in range(4)]
# print(matrix_column)

column_mean = []
for i in range(4):
    added = 0
    for j in range(4):
        added += matrix_column[j][i]
    column_mean.append(added/len(matrix_column))
print(column_mean)