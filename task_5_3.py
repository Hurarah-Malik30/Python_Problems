def checksubstring():
    # list_substring = ['a', 'abb', 'sfs', 'oo', 'de', 'sfde']
    list_substring = ['a', 'abb', 'sad', 'ooaaesdfe', 'sfsdfde', 'sfsd', 'sfsdf', 'qwrew']
    length =len(list_substring)
    if(list_substring[length-2] in list_substring[length - 1]):
        return True
    else:
        return False

print(checksubstring())