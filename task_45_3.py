def getEvenpalinfromes(n):
    res_palindrome = []
    for i in range(n+1):
        if((i%2==0)and(str(i) == (str(i))[::-1])):
            res_palindrome.append(i)
    return res_palindrome

print(getEvenpalinfromes(50))
print(getEvenpalinfromes(100))
