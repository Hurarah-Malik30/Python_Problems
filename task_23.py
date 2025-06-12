
def makeN_Copies(var,num):
    if len(var) > 2:
        for i in range(num):
            print(var[0] + var[1],end=",")
    elif len(var) <= 2:
        for i in range(num):
            print(var,end=",")

makeN_Copies("harry",3)
makeN_Copies("sa",3)