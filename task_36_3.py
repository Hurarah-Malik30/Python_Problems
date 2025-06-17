def getKlargest(list_nums_k,k):
    resultant_k_large = []
    list_nums_k.sort(reverse=True)
    for i in range(k):
        resultant_k_large.append(list_nums_k[i])
    return resultant_k_large

print(getKlargest([1, 2, 3, 4, 5, 5, 3, 6, 2],1))
print(getKlargest([1, 2, 3, 4, 5, 5, 3, 6, 2],2))
print(getKlargest([1, 2, 3, 4, 5, 5, 3, 6, 2],3))
print(getKlargest([1, 2, 3, 4, 5, 5, 3, 6, 2],4))
print(getKlargest([1, 2, 3, 4, 5, 5, 3, 6, 2],5))
