operators = '+-*/'
priority = {
    '+' : 0,
    '-' : 0,
    '*' : 1,
    '/' : 1
}

def test_priority(operator1 , operator2):
    return priority[operator1] >= priority[operator2]

print(test_priority('/','-'))