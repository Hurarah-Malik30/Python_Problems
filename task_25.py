list_of_numbers = [1,5,8,3]

def checkNumber(num):
    if num in list_of_numbers:
        print("Number exist in list")

    else:
        print("Number does not exist in list")


checkNumber(3)
checkNumber(-1)
checkNumber(1)
checkNumber(10)