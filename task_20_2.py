def getTrailingZero(n):
    x = n // 5
    y = x

    while x > 0:
        x = x / 5
        y += int(x)
    return y

print(getTrailingZero(5))
print(getTrailingZero(12))
print(getTrailingZero(100))
