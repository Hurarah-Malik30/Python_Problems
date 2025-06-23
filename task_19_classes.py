class ReverseString:
    def getreverse(s):
        return ' '.join(reversed(s.split()))
p1 = ReverseString
print(p1.getreverse("hello .py"))