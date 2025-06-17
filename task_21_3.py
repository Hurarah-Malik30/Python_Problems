def lastletter(list_last):
    last_listresult = []
    for i in list_last:
        if (i[-2] == ' '):
            last_listresult.append(True)
        else:
            last_listresult.append(False)
    return last_listresult

print(lastletter(['cat', 'car', 'fear', 'center']))
print(lastletter(['ca t', 'car', 'fea r', 'cente r']))