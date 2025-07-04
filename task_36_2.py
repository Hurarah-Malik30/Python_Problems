def round_n(n):
    if n % 1000:
        return (1 + n // 1000) * 1000
    else:
        return n

def compute_debt(n):
    if n == 0:
        return 100000
    return int(round_n(compute_debt(n-1)*1.05))

months = int(input("Input No of Months: "))
result = compute_debt(months)
print("Amount:",result)