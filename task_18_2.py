
x = input("Input the first number: ")
y = input("Input the second number: ")
z = input("Input the third number: ")
print("Median of the above three numbers -")

if y < x < z:
    print("X: ", x , " is the median..")
elif y > x > z:

     print("X: ", x , " is the median..")
elif x < y < z:
    print("Y: ", y , " is the median..")
elif x > y > z:
     print("Y: ", y , " is the median..")

elif x < z < y:
    print("Z: ", z , " is the median..")
elif x > z > y:
     print("Z: ", z , " is the median..")
    