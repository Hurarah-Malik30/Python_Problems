def checkoverflow(a,b):
    sum = a + b
    if(sum >= 10 ** 80 or a >= 10 ** 80 or b >= 10 ** 80):
        print("Overflow")
    else:
        print("Sum:",sum)

checkoverflow(25,22)
