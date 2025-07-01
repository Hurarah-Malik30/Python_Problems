res = []
for i in range(100,401):
    x = str(i)
    for y in x:
        flag = True
        if int(y) % 2 != 0:
            flag = False
            break
    if flag:
        res.append(i)

print(res)