rows = int(input("Enter rows:"))
columns = int(input("Enter columns:"))

matrix = []

for i in range(rows):
    row = []
    for j in range(columns):
        element = int(input(f"Enter element at position ({i+1}, {j+1}): "))
        row.append(element)
    matrix.append(row)
    
for row in matrix:
    print(row)