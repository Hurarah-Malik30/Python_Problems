lst = [2, 5, 8, 12, 15]

odded_list = [x+1 if x%2==0 else x for x in lst]
print(odded_list)