class power:
    def getpow(self,x,n):
        if x == 0 or x == 1 or n == 1:
            return x
        if x == -1:
            if n%2 == 0:
                return 1
            else:
                return -1
        if n==0:
            return 1
        if n<1:
            return 1/self.getpow(x,-n)
        val = self.getpow(x,n//2)
        if n%2 ==0:
            return val*val
        return val*val*x

p1 = power()
print(p1.getpow(2,5))