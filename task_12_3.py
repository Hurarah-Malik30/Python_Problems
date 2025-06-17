def checkPalindromes(list_palindrome):
    result_list = []
    for i in list_palindrome:
        if i == i[::-1]:
            result_list.append(True)
        else:
            result_list.append(False)
    return result_list

pal_list = ['palindrome', 'madamimadam', '', 'foo', 'eyes']
print(checkPalindromes(pal_list))