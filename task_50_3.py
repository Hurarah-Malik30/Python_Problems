def evenlength(arr):
    res = []
    for i in range(len(arr)):
        if(len(arr[i]) % 2 == 0):
            res.append(arr[i])
    res.sort(key=len)
    return res



print(evenlength(['Red', 'Black', 'White', 'Green', 'Pink', 'Orange']))
print(evenlength(['The', 'worm', 'ate', 'a', 'bird', 'imagine', 'that', '!', 'Absurd', '!!']))