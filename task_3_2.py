nums_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

for i in nums_list: 
    if i % 3 == 0:
        print(i)
        nums_list.remove((i))

# print(nums_list)