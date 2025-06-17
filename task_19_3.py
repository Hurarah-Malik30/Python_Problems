def splitString(s):
     if ' ' in s:
        return s.split()
     elif ',' in s:
        return s.split(',')
     else:
        return [c for c in s if c.islower() and ord(c) % 2 == 0]

print(splitString('a,b,c,d'))
print(splitString('abcd'))
    