import re

password = input("Enter a password: ")
x = True

while True:
    if (len(password) < 6 or len(password) > 16):
        break
    elif not re.search('[a-z]', password):
        break
    elif not re.search('[A-Z]', password):
        break
    elif not re.search('[0-9]', password):
        break
    elif not re.search("[$#@]", password):
        break
    elif re.search(r'\s', password):
        break
    else:
        print("Valid Password")
        x = False
        break

if x:
    print("Invalid Password")
