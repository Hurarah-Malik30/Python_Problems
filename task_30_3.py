def getfewerchar(list_string1):
    char_1 = 0
    char_2 = 0
    for i in list_string1[0]:
        for j in i:
            char_1 += 1
    for i in list_string1[1]:
        for j in i:
            char_2 += 1
    if char_1 < char_2:
        return list_string1[0]
    else:
        return list_string1[1]

print(getfewerchar([['this', 'list', 'is', 'narrow'], ['I', 'am', 'shorter but wider']]))
print(getfewerchar([['Red', 'Black', 'Pink'], ['Green', 'Red', 'White']]))
