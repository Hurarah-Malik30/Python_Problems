res_P = ""

for row in range(0,7):
    for column in range(0,6):
        if((column == 0) or ((column == 1 or column == 2 or column == 3) and  (row == 0 or row == 3)) or ((row == 1 or row == 2) and column == 4)):
            res_P = res_P + "*"
        else:
            res_P = res_P + " "
    res_P = res_P + "\n"
print(res_P)