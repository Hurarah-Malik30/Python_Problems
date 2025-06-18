lst1 = [1, 2, 3]
lst2 = [4, 5, 6]

ans_list = [(x-y)**2 for x,y in zip(lst1,lst2)]
print(ans_list)