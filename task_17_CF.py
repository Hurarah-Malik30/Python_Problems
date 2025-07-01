res_A = ""

for row in range(0,8):
    for column in range(0,5):
        if (((column == 0 or column == 4) and (row == 1 or row == 2 or row == 3 or row == 4 or row == 5 or row == 6 or row == 7)) or ((column == 1 or column == 2 or column == 3)and(row == 0 or row == 4))):
            res_A = res_A + "*"   
        else:
            res_A = res_A + " "
    res_A = res_A + "\n"
    
print(res_A)