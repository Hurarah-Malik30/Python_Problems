digit_count = 0
alpha_count = 0

s = input("Enter a string:")

for i in range(len(s)):
    if s[i].isdigit():
        digit_count += 1
    elif s[i].isalpha():
        alpha_count += 1
        
print("Digits:",digit_count,"Alphabets Count:",alpha_count)