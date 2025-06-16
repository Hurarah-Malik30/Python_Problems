import math
def getCDs(x,y):
    n = math.gcd(x,y)
    result = 0
    z = int(n**0.5)
    i = 1
    while(i <= z):
        if(n % i == 0):
            result += 2
            if(i == n/i):
                result -= 1
        i += 1
    return result

print(getCDs(2,4))
print(getCDs(2,8))