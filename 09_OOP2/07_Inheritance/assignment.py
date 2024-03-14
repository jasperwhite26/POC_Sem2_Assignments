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
 
    def __str__(self) -> str:
        return "Rectangle with base: " + str(self.__base) + ", height" + str(self.__height)

class Square(Rectangle):
    def __init__(self, side_length:float) -> None:
        super().__init__(side_length, side_length)
        self.__side_length = side_length

    def get_side_length(self) -> float:
        return self.__side_length
    
    def __str__(self)-> str:
        return "Square with side length" + str(self.__side_length)

square1 = Square(3)
print(square1)
print("The base of square1 is", square1.get_base())
print("The height of square1 is", square1.get_height())
print("The side length of square1 is", square1.get_side_length())
print("The area of square1 is", square1.get_area())
print("The perimeter of square1 is", square1.get_perimeter())