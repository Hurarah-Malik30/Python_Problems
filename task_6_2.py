
para = "The cat ran fast. The dog ran faster. The cat jumped high. The dog barked. The cat meowed. The cat and dog ran together through the park happily."
print(para)

list_of_words = para.split()

print(list_of_words)

for word in list_of_words:
    x = list_of_words.count(word)
    print("Count of word " , word , " is: " , x)