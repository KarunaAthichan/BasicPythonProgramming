import math

# Create a class Circle
class Circle:

    # Creating property or data for class Circle
    def __init__(self, radius, colour):
        # object/instance variable = local variable
        self.radius = radius
        self.colour = colour

    # creating behaviour or function for class Circle
    def getRadius(self):
        return self.radius

    def setRadius(self,radius):
        self.radius = radius

    def getColour(self):
        return self.colour

    def getArea(self):
        return math.pi * math.pow(self.radius,2)


print("value for Circle C1")
# creating object Circle c1
c1 = Circle(3.1, "red")
print(c1.getRadius())
print(c1.getArea())
c1.setRadius(5)
print("Updated radius via setRadius ",c1.getRadius())
print("Updated area after new Radius ",c1.getArea())
print(c1.getColour())


print("*"*27)

print("value for Circle C2")
# creating object Circle c2
c2 = Circle(4, "green")
print(c2.getRadius())
print(c2.getColour())
print(c2.getArea())




