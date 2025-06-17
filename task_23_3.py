def list_decrease(list_dec):
    indices_dec = []
    for i in range(len(list_dec)):
        if(list_dec[i] < list_dec[i-1]):
            indices_dec.append(i)
    return indices_dec

print(list_decrease([0, -1, 3, 8, 5, 9, 8, 14, 2, 4, 3, -10, 10, 17, 41, 22, -4, -4, -15, 0]))
print(list_decrease([6, 5, 4, 3, 2, 1]))