def digitsSum(n):
    return sum(int(d) for d in str(n))
def sortBySum(list_sum_sort):
    return sorted(list_sum_sort, key=digitsSum)
print(sortBySum([10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))