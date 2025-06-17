def getindices(nums_list,n):
    res_list = []
    for i in range(len(nums_list)):
        if nums_list[i] < 100:
            res_list.append(i)

    return res_list

a = [0, 12, 45, 3, 4923, 322, 105, 29, 15, 39, 55]
print(getindices(a,100))