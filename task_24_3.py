def maxithelement(list_max):
    for i in range(len(list_max)):
        if(list_max[i] < list_max[i-1]):
            list_max[i] = list_max[i-1]
    return list_max

print(maxithelement([0, -1, 3, 8, 5, 9, 8, 14, 2, 4, 3, -10, 10, 17, 41, 22, -4, -4, -15, 0]))
print(maxithelement([6, 5, 4, 3, 2, 1]))    
print(maxithelement([1, 19, 5, 15, 5, 25, 5]))
