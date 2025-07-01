res_O = ""

for row in range(0,8):
    for column in range(0,5):
        if(((column == 0 or column == 4)and(row == 1 or row == 2 or row == 3 or row == 4 or row == 5 or row == 6)) or ((row == 0 or row == 7) and (column == 1 or column == 2 or column == 3))):
            res_O = res_O + "*"
        else:
            res_O = res_O + " "
    res_O = res_O + "\n"            
    
print(res_O)
