
def is_closeto_thousand(num):
    return ((abs(1000 - num) <=100) or (abs(2000 - num) <= 100))

print(is_closeto_thousand(900))
print(is_closeto_thousand(2200))