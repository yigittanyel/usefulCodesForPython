from abc import ABC,abstractmethod
import math

class Shape(ABC):
    """Super Class"""
    def toString(self):
        print("Shapes")
    
    @abstractmethod
    def area(self):pass

    @abstractmethod
    def perimeter(self):pass

class Square(Shape):
    "Square Class"
    def __init__(self,edge):
        self.__edge=edge

    def area(self):
        result=self.__edge**2
        print("Area of square %f" %(result))

    def perimeter(self):
        result=self.__edge*4
        print("Perimeter of square %d" %(result))

    def toString(self):
        print("Square edge: %d" %(self.__edge))

class Circle(Shape):
    """Circle Class"""
    def __init__(self,radius):
        self.__radius=radius

    def area(self):
        result=math.pi*((self.__radius)**2)
        print("Area of circle {:.2f}".format(result))
    def perimeter(self):
        result=2*math.pi*self.__radius
        print("Perimeter of circle {0:.2f}".format(result))

    def toString(self):
        print("Circle radius {}".format(self.__radius))

sq=Square(5)
cr=Circle(4)

sq.area()
cr.perimeter()
sq.toString()
cr.toString()

print(Shape.__doc__)
print(Square.__doc__)