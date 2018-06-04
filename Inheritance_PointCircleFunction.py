import math

# creating parent class Point
class Point:
    # declaring a protected variable, only single underscore. Only Public and Protected
    # variables can be used in child/sub/derived class
    _x = 0
    _y = 0

    # initialising local variables
    def __init__(self, x, y):
        # self.protected variable  = local variable
        self._x = x
        self._y = y

    # define setvalue functions
    def setValueX(self, xval):
        self._x = xval

    def setValueY(self, yval):
        self._y = yval

    # define getvalue functions
    def getValueX(self):
        return self._x

    def getValueY(self):
        return self._y


# creating child class Circle which inherits from parent class Point
class Circle(Point):
    # declaring private variable
    __radius = 0

    # initialising local variable, where x and y are from parent class
    def __init__(self, x, y, radius):
        # use super() function to call variables of parent class Point
        super().__init__(x, y)
        self.__radius = radius

    # defining calculate area function
    def calculateArea(self):
        return math.pi * self.__radius ** 2


# create instance for Point class
point = Point(10, 20)

# setValueX and setValueY replace the value mentioned in Point instance value declaration
point.setValueX(1)
point.setValueY(2)

print(point.getValueX())
print(point.getValueY())

# create instance for Circle class
circle = Circle(2, 3, 20)
# print the area of circle
print(circle.calculateArea())

# identify the members of Point and Circle class by calling instance and dictionary
print("Point members ", point.__dict__)
print("Circle members ", circle.__dict__)