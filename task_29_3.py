def findIndices(list_sum):
    index_list = []
    for i in range(len(list_sum)):
        for z in range(i,len(list_sum)):
            if list_sum[i] + list_sum[z] == 0:
                index_list.append(i)
                index_list.append(z)
    return index_list

print(findIndices([1, -4, 6, 7, 4]))
print(findIndices([1232, -20352, 12547, 12440, 741, 341, 525, 20352, 91, 20]))