def getpalendrome(n):
    num_list = []
    for i in range(10**(n-1),10**n):
        z = str(i)
        if z == z[::-1]:
            num_list.append(z)
    return num_list
print(getpalendrome(4))