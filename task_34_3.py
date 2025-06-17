def calculateSumuptoK(list_sum_k,k):
    sum_k = 0
    for i in range(k):
        if(100 <= abs(list_sum_k[i]) <= 999):
            sum_k += list_sum_k[i]
    return sum_k

print(calculateSumuptoK([114, 215, -117, 119, 14, 108, -9, 12, 76],5))
print(calculateSumuptoK([4, 5, 17, 9, 14, 108, -9, 12, 76],4))