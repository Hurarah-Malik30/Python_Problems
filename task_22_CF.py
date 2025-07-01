res_M = ""

for row in range(0,8):
    for column in range(0,6):
        if ((column == 0 or column == 4) or (row == 2 and (column == 1 or column == 3)) or (row == 3 and column == 2)):
            res_M = res_M + '*'
        else:
            res_M = res_M + " "
    res_M = res_M + '\n'
    
print(res_M)