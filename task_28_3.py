def uniqueword(list_unique):
    for i in range(len(list_unique)):
        new_word = ''
        seen = set()
        for j in list_unique[i]:
             if j not in seen:
                seen.add(j)
                new_word += j
        list_unique[i] = new_word
    max_length = ''
    for i in list_unique:
        if len(i) > len(max_length):
            max_length = i
    return max_length
    

print(uniqueword(['cat', 'catatatatctsa', 'abcdefhijklmnop', '124259239185125', '', 'foo', 'unique']))
print(uniqueword(['Green', 'Red', 'Orange', 'Yellow', '', 'White']))