def carrycounter(x,y):
    counter = 0
    if (x == 0 and y == 0):
        return 0
    z = 0
    while x > 0 or y > 0:
        z = x % 10 + y % 10 + z

        if z > 9:
            z = 1
        else:
            z = 0
        counter += z

        x //= 10
        y //= 10

    if counter == 0:
        return 'NO Carry Operation'
    elif counter == 1:
        return counter
    else:
        return counter

print(carrycounter(786,457))