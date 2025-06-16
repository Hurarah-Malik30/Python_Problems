def getsumpalindrome(n):
    sum = 0
    while True:
        k = str(n)
        if k == k[::-1]:
            break
        else:
            m = int(k[::-1])
            n += m
            sum += 1
    return n

print(getsumpalindrome(1234))
print(getsumpalindrome(1473)) 
    