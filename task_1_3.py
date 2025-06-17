# list_of_nums = [19, 19, 15, 5, 3, 5, 5, 2]
list_of_nums = [19, 15, 15, 5, 3, 3, 5, 2]

count_19 = list_of_nums.count(19)
count_5 = list_of_nums.count(5)

if(count_19 == 2 and count_5 >= 3):
    print("True")
else:
    print("False")