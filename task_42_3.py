def getdistinct(s):
    distinct_list = []
    seen = set()
    for i in s: 
        if i not in seen:
            distinct_list.append(i)
            seen.add(i)
    return distinct_list
print(getdistinct('HELLO'))
print(getdistinct('Ignoring case'))