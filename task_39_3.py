def calculateTripleSum(list_sum_triple):
    resultant_triple_sum = []
    for i in range(len(list_sum_triple)):
        sum = 0
        for j in range(len(list_sum_triple[i])):
            sum += list_sum_triple[i][j]
        if(sum == 0):
            resultant_triple_sum.append(True)
        else:
             resultant_triple_sum.append(False)
    return resultant_triple_sum


print(calculateTripleSum([[1343532, -2920635, 332], [-27, 18, 9], [4, 0, -4], [2, 2, 2], [-20, 16, 4]]))
print(calculateTripleSum([[1, 2, -3], [-4, 0, 4], [0, 1, -5], [1, 1, 1], [-2, 4, -1]]))