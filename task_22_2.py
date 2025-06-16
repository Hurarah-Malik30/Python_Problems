
def getsumof4(n):
    if n == 1 or n == 2 or n == 3 or n == 4:
        return 1
    else:
        return getsumof4(n-1) + getsumof4(n-2) + getsumof4(n-3) + getsumof4(n-4)
print(getsumof4(5))
print(getsumof4(6))
print(getsumof4(7))