res_G = ""

for row in range(0,7):
    for column in range(0,7):
        if ((row != 0 and row != 6 and column == 1) or ((row == 0 or row == 6) and column > 1 and column < 5)or (row == 3 and column > 2 and column < 6) or (column == 5 and row != 0 and row != 2 and row != 6)): 
            res_G = res_G + "*"
        else:
            res_G = res_G + " "
            
    res_G = res_G + "\n"
    
print(res_G)