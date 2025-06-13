with open("example.txt",'r') as f:
    list_of_letters = [letter for word in f for letter in word if letter != ' ']

for i in list_of_letters:
    print("Count of letter " , i , " is" , list_of_letters.count(i))
