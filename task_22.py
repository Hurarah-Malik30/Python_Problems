list_of_Numbers =[1,4,2,4,3,4,5,4,6,4,7,4,8,4,9,4]

count_of_4 = 0

for i in list_of_Numbers:
    if (i == 4):
        count_of_4 += 1
    else:
        continue

print("Count is: " + str(count_of_4))