import task_31

def calculate_LCM(x,y):
    res = task_31.calculate_GCD(x,y)
    lcm = (x*y) // res
    return lcm

print(calculate_LCM(4,6))
print(calculate_LCM(15,17))