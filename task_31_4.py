import random
matrix = [[random.random() for _ in range(3)] for _ in range(3)]
print(matrix)
matrix = [[1 if x > 0.5 else 0 for x in row]for row in matrix]
print(matrix)