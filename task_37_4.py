lst = [1, 2, 3, 4, 5]
flag = True
for i in lst:
    if i == 0:
        flag = False
        break
print(flag)