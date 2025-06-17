def interpretXOR(num):
    xor = bin(int(num[0],2) ^ int(num[1],2))
    return xor

print(interpretXOR(['0001','1011']))
print(interpretXOR(['100011101100001', '100101100101110']))