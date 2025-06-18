lst = [10, 20, 30, 40, 50]
percentage_25 = sorted(lst)[int(len(lst) * 0.25)]
percentage_75 = sorted(lst)[int(len(lst) * 0.75)]
new_list = [0 if percentage_25 <= x <= percentage_75 else x for x in lst]
print(new_list)