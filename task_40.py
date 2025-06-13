import math

point1 = [4,0]
point2 = [6,6]

def calculateDistance(p1,p2):
    return (round(math.sqrt(((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2)),2))

print(calculateDistance(point1,point2))