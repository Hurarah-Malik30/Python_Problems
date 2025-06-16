user_input = input("Enter x1,y1,x2,y2,x3,y3 with a space: ")
x1,y1,x2,y2,x3,y3 = map(float,user_input.split())
c = (x1 - x2)**2 + (y1 - y2)**2
a = (x2 - x3)**2 + (y2 - y3)**2
b = (x3 - x1)**2 + (y3 - y1)**2

s = 2 * (a * b + b * c + c * a) - (a**2 + b**2 + c**2)

px = (a * (b + c - a) * x1 + b * (c + a - b) * x2 + c * (a + b - c) * x3) / s
py = (a * (b + c - a) * y1 + b * (c + a - b) * y2 + c * (a + b - c) * y3) / s

ar = a**0.5
br = b**0.5
cr = c**0.5
r = ar * br * cr / ((ar + br + cr) * (-ar + br + cr) * (ar - br + cr) * (ar + br - cr))**0.5

print("Radius of the said circle:",r)

print("Central coordinate (x, y) of the circle:",px,"&",py)