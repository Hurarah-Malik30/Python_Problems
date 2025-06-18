import random
sum_list = [[random.random() for x in range(3)]for y in range(3)]
addition = sum(sum_list[i][i] for i in range(3))
print(addition)