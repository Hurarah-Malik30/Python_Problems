import random
random_list = [[random.random() for x in range(3)]for y in range(3)]
# print(random_list)

sorted_matrix = [sorted(row) for row in random_list]

print(sorted_matrix)