def getvalidate(list_number):
    length = len(list_number)
    fifth = list_number[4]
    count = list_number.count(fifth)
    if(length == 8 and count == 3):
        return True
    else:
        return False

# a = [19, 19, 15, 5, 5, 5, 1, 2]
a = [19, 15, 5, 7, 5, 5, 2]

print(getvalidate(a))