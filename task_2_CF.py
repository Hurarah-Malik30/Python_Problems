choice = input('Do yow want to convert to Celsius or Farenheit-[C/F]: ')
while ((choice != 'C') and (choice != 'c') and (choice != 'F') and (choice != 'f')):
    choice = input('Please Enter a valid choice-[C/F]: ')
if ((choice == 'C') or (choice == 'c')):
    f = int(input('Enter temperature in Farenheit: '))
    print(round(((f-32)*5)/9,2))
elif ((choice == 'F') or (choice == 'f')):
    c = int(input('Enter temperature in Celsius: '))
    print(round((c*(9/5))+32,2))

    