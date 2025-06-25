class Rectangle:
    def __init__(self,l,w):
        self.l = l
        self.w = w
        
    def Compute_Area(self):
        return self.l*self.w
    
r1 = Rectangle(10,10)
print(r1.Compute_Area())