color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])


print("Difference of first set with second:")
res_list = set(color_list_1.difference(color_list_2))
print(res_list)
print("Difference of second set with first:")
res_list = set(color_list_2.difference(color_list_1))
print(res_list)