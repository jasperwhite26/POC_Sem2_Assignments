class RightTriangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return 1/2 * self.base * self.height
        

triangle1 = RightTriangle(3, 4)
print("The area of triangle1 is", triangle1.area())

triangle2 = RightTriangle(4, 10)
print("The area of triangle2 is", triangle2.area())  

