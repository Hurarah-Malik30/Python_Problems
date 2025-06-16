import math
def rightTriangle(a,b,c):
    a_2 = pow(a,2)
    b_2 = pow(b,2)
    c_2 = pow(c,2)
    if((a_2 == b_2 + c_2) or (b_2 == a_2 + c_2) or (c_2 == a_2 + b_2)):
        return "Right Triangle..."
    else:
        return "Not A Right Triangle..."
print(rightTriangle(8,6,7))