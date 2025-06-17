def checkPrefix(a,list_prefix):
    result_prefix = []
    for i in list_prefix:
        if( i[0] == a[0] and (i[1] == a[1])):
            result_prefix.append(i)
    return result_prefix

print(checkPrefix('ca',('cat', 'car', 'fear', 'center')))
print(checkPrefix('do',('cat', 'dog', 'shatter', 'donut', 'at', 'todo')))