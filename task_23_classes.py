from math import pi
class Circle:
    def __init__(self,r):
        self.r = r
        
    def Compute_Area(self):
        return (pi*(self.r**2))
    
    def Compute_Perimeter(self):
        return (2*pi*self.r)
    
c1 = Circle(10)
print(c1.__class__)