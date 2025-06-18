import random
matrix = [[random.random() for _ in range(3)] for _ in range(3)]
# print(matrix)
max_indexes = [row.index(max(row)) for row in matrix]
print(max_indexes)