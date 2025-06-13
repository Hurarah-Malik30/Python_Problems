def checkequityAndFive(a,b):
    if ((a==b) or (a+b == 5) or (b+a == 5) or (a-b == 5) or (b-a == 5)):
        return True
    else:
        return False

print(checkequityAndFive(5,5))
print(checkequityAndFive(3,2))
print(checkequityAndFive(7,2))
print(checkequityAndFive(10,20))