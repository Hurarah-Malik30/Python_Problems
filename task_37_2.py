import itertools

def getcount(n):
    counter = 0
    for a in range(10):
        for b in range(10):
            for c in range(10):
                for d in range(10):
                    if a+b+c+d == n:
                        counter+=1
    return counter


num = int(input("Enter a number: "))
if 0 <= num <= 50:
    result = getcount(num)
    print(f"Number of combinations for sum {num} is: {result}")
else:
    print("Invalid input. n must be between 0 and 36.")

