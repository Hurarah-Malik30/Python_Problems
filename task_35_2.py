user_inp = (input("Enter values of a,b,c,d,e,f separated by space: "))
a,b,c,d,e,f = map(float,user_inp.split())

n = a * e - b * d

if n != 0:
    x = (c * e - b * f) / n
    y = (a * f - c * d) / n

print("X: ",x)
print("Y: ",y)