class Cat:

    # class or static variable doesn't start with underscore
    kind = "Feline"

    # instance or object variable
    __name=""

    # creating static variable
    count = 0

    # initialising a function with local variable
    def __init__(self,name):
        # object or instance variable = local variable
        self.__name=name
        # classname.class or static variable
        Cat.count += 1

    # defining getName function
    def getName(self):
        return self.__name

    # defining getKind function
    def getKind(self):
        return self.kind

print("Value of count before object", Cat.count)
# object declaration
c1 = Cat("max")
print("Value of count after object1", Cat.count)
c2 = Cat("oreo")
print("Value of count after object2", Cat.count)

print(c1.getName())
print(c2.getName())

print(c1.getKind())
print(c2.getKind())