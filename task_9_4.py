matrix = [[1,2,3],[4,5,6],[7,8,9]]
sum = 0


for row in range(3):
    for element in range(3):
        if row == element:
            sum += matrix[element][row]

print(sum)