def checkincreasing(num_increase):
    flag = []
    for i in range(0,len(num_increase)-1):
        if(num_increase[i] > num_increase[i+1]):
            flag.append(i)
            flag.append(i+1)
    return flag

print(checkincreasing([1, 2, 3, 0, 4, 5, 6]))
print(checkincreasing([1, 2, 3, 4, 5, 6]))
print(checkincreasing([-3, -2, -3, 0, 2, 3, 4]))
