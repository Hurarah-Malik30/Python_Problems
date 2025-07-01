res = []
while True:
    l = input("Enter a line or hit enter to break:")
    
    if l:
       res.append(l.lower()) 
    else:
        break
    
for l in res:
    print(l)