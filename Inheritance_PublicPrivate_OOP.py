''' Write an object oriented program that performs the following tasks:
1. Create a class called Chair from the base class Furniture
2. Teakwood should be the type of furniture that is used by all furnitures by default
3. The user can be given an option to change the type of wood used for chair if he wishes to
4. The number of legs of a chair should be a property that should not be altered outside the class '''


# Base class
class Furniture:
    typeofwood = "Teakwood"


# Derived class
class Chair(Furniture):
    __numberoflegs = 4

    def __init__(self, typeofwood=None):
        # when there is no attribute passed in instance creation, take the base class attribute
        if typeofwood is None:
            typeofwood = self.typeofwood
        else:
            self.typeofwood = typeofwood
        print("The chair is made of {} and it has {} legs".format(self.typeofwood, self.__numberoflegs))


# Derived class
class Table(Furniture):
    _numberoflegs = 6

    def __init__(self):
        print("The table is made of {} and it has {} legs".format(self.typeofwood, self._numberoflegs))


# Instance creation
chair = Chair("Plywood")
table = Table()