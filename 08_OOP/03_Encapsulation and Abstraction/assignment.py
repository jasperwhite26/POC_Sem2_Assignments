class Rectangle:
    def __init__(self, base: float, height: float) -> None:
        if(base < 0):
            self.__base = 0
        else:       
            self.__base = base
            
        if(height < 0):
            self.__height = 0
        else:
            self.__height = height
        
    def get_height(self) -> float:
        return self.__height
    
    def get_base(self) -> float:
        return self.__base
    
    def get_perimeter(self) -> float:
        return 2 * self.__base + 2 * self.__height
    
    def get_area(self) -> float:
        return self.__base * self.__height
 
 
 
rect1 = Rectangle(3, 4)
print("The base of rectangle1 is", rect1.get_base())
print("The height of rectangle1 is", rect1.get_height())
print("The perimeter of rectangle1 is", rect1.get_perimeter())
print("The area of rectangle1 is", rect1.get_area())

rect2 = Rectangle(10, 22)
print("The base of rectangle2 is", rect2.get_base())
print("The height of rectangle2 is", rect2.get_height())
print("The perimeter of rectangle2 is", rect2.get_perimeter())
print("The area of rectangle2 is", rect2.get_area())