def getlargestdivisor(n):
    largestdivisor = 0
    for i in range(n-1,0,-1):
        if(n % i == 0):
            largestdivisor = i
            break
    return largestdivisor

print(getlargestdivisor(18))
print(getlargestdivisor(100))
print(getlargestdivisor(102))
print(getlargestdivisor(500))