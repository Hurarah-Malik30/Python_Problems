def getVowels(s):
    indices_list_vowels = []
    vowels_upper = ['A','E','I','O','U']
    for i in range(len(s)):
        if ((s[i] in vowels_upper) and i % 2 == 0):
            indices_list_vowels.append(i)
    return indices_list_vowels

print(getVowels('w3rEsOUrcE'))
print(getVowels('AEIOUYW'))

