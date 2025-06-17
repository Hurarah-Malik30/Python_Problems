def getlength(list_words):
    list_length = []
    for i in range(len(list_words)):
        list_length.append(len(list_words[i]))
    return list_length
print(getlength(['cat', 'car', 'fear', 'center']))
