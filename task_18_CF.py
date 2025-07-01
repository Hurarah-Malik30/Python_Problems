res_D = ""

for row in range(0,8):
    for column in range(0,6):
        if (((row == 0 or row == 7) and (column == 1 or column == 2 or column == 3 or column == 4)) or ((column == 1 or column == 5) and (row == 1 or row == 2 or row == 3 or row == 4 or row == 5 or row == 6))):
            res_D = res_D + "*"
        else:
            res_D = res_D + " "
    res_D = res_D + '\n'
    
print(res_D)