def futureValueCalculate(amount,interest,year):
    return(amount * (1 + (0.01 * interest)) ** year)

print(round(futureValueCalculate(10000,3.5,7),2))