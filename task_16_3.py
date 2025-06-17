def checksubString(a,list_sub):
    final_Sub = []
    for i in list_sub:
        if a in i:
            final_Sub.append(i)
    return final_Sub

print(checksubString('ca',('cat', 'car', 'fear', 'center')))
print(checksubString('o',('cat', 'dog', 'shatter', 'donut', 'at', 'todo', '')))
