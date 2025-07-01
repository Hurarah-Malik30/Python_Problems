res = []

for x in range(1500,2701):
    if ((x % 5 == 0) and (x % 7 == 0)):
        res.append(str(x))
        
print(','.join(res))