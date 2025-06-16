def getnonpositive(n):
    while n > 0:
        digit_sum = sum([int(d) for d in list(str(n))])
        n = n - digit_sum
    return n


print(getnonpositive(20))     
print(getnonpositive(110))    
print(getnonpositive(5674))   
