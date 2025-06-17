def calculateAsciiSum(word_ascii):
    sum = 0
    for i in word_ascii:
        if i.isupper() == True:
            sum += ord(i)
    return sum
print(calculateAsciiSum('PytHon ExerciSEs'))
print(calculateAsciiSum('JavaScript'))