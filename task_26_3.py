def maxnum(list_num_max):
    for i in range(len(list_num_max)):
        list_num_max[i] = list_num_max[i].replace(',','.')
    return max(list_num_max)

print(maxnum(['100', '102,1', '101.1']))