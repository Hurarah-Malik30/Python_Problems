a = 10
b = 30

while b != 0:
    carry = a & b
    a = a ^ b
    b = carry << 1
print(a) 