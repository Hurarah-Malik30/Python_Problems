#list and tupel generator

numbers = input("Enter comma separated numbers: ")
listofNumbers = numbers.split(',')
tupleofNumbers = tuple(listofNumbers)
print('List: ',listofNumbers)
print('Tuple: ',tupleofNumbers)