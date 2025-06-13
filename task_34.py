def getsum(a,b):
    res = a+b
    if (res >= 15 and res <= 20 ):
        return 20
    else:
        return res

print(getsum(10,6))
print(getsum(10,12))