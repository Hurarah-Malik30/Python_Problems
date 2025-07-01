bin_list = [x for x in input("Enter numbers separated by comma:").split(',')]
res = []
for i in bin_list:
    x = int(i,2)
    if x % 5 == 0:
        res.append(i)
        
print(','.join(res))
        