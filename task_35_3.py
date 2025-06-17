def calculateproduct_odd(n):
    product = 1
    found = False
    n_str = str(n)
    for i in n_str:
        if (int(i) % 2 != 0):
            product *= int(i)
            found = True
    return product if found else 0

print(calculateproduct_odd(123456789))
print(calculateproduct_odd(2468))
print(calculateproduct_odd(13579))

