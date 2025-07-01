import random

rand = random.randint(1,10)
# print(rand)
guess = int(input("Guess a number between 1-10: "))

while guess != rand:
    guess = int(input("Guess again: "))
    
print("Well Guessed!")