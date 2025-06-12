
def addIs(var):
    if ((var[0] == 'I' or var[0] == 'i') and (var[1] == 'S' or var[1] == 's')):
        return var

    else:
        newVar = "Is" + var
        return newVar


print(addIs("iSAli"))
print(addIs('ali'))
