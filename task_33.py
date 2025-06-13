def sumwithequity(a,b,c):
    if ((a==b) or (b==c) or (a==c)):
        return 0

    else:
        return (a+b+c)

print(sumwithequity(1,2,3))
print(sumwithequity(2,1,2))