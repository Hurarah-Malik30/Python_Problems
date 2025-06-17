def getHindex(list_H_ind):
    h_ind = -1
    unique_list = set(list_H_ind)
    for i in unique_list:
        if list_H_ind.count(i) == i:
            h_ind = i
    return h_ind


print(getHindex([1, 2, 2, 3, 3, 4, 4, 4, 4]))
print(getHindex([1, 2, 2, 3, 4, 5, 6]))