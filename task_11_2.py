import itertools

X = [10, 20, 20, 20]
Y = [10, 20, 30, 40]
Z = [10, 30, 40, 20]


combination_X_3 = [list(i) for i in itertools.combinations(X,3)]
combination_Y_3 = [list(i) for i in itertools.combinations(Y,3)]
combination_Z_3 = [list(i) for i in itertools.combinations(Z,3)]

print('\nFor X-List Combinations:\n')

for i in combination_X_3:
    sum = 0
    for z in i:
        sum += z
    if(sum == 70):
        print('The Combination Of X_List', i , 'has sum = 70')
    else:
        print('Sum of Combination Of X_List: ' ,i , 'is not 70')

print('\nFor Y-List Combinations:\n')

for i in combination_Y_3:
    sum = 0
    for z in i:
        sum += z
    if(sum == 70):
        print('The Combination Of Y_List', i , 'has sum = 70')
    else:
        print('Sum of Combination Of Y_List: ' ,i , 'is not 70')

print('\nFor Z-List Combinations:\n')

for i in combination_Z_3:
    sum = 0
    for z in i:
        sum += z
    if(sum == 70):
        print('The Combination Of Z_List', i , 'has sum = 70')
    else:
        print('Sum of Combination Of Z_List: ' ,i , 'is not 70')