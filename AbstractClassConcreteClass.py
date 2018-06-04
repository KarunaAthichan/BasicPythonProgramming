# Abstract Class

# Abstract Base Class and Abstract method import
from abc import ABC, abstractmethod

# Animal class inherit from ABC class
class Animal(ABC):

    # create initialiser function
    def __init(self, name):
        self.__name = name

    # create abstract method, it shouldn't have any information
    @abstractmethod
    def makeNoise(self):
        pass

    # create abstract method
    @abstractmethod
    def eat(self):
        pass

    # non abstract method, so we can write body of function
    # abstract class may have non abstract method, but abstract class cannot be instantiated
    def move(self):
        print("I can move anywhere")


# create a Lion class which inherits from Animal abstract class
class Lion(Animal):

    # create initialiser function
    def __init__(self, name):
        # call the parent class variable
        super().__init__()

    # call abstract class method and enter the body under Lion class
    def makeNoise(self):
        print("I can roar...")

    # call abstract class method and enter the body under Lion class
    def eat(self):
        print("I can eat buffaloes, Zebras")


# create a Cat class which inherits from Animal abstract class
class Cat(Animal):

    # create initialiser function
    def __init__(self, name):
        # call the parent class variable
        super().__init__()

    # call abstract class method and enter the body under Lion class
    def makeNoise(self):
        print("Meow meow...")

    # call abstract class method and enter the body under Lion class
    def eat(self):
        print("I can eat mouses")


# crete objects of Lion and Cat classes
lion = Lion("Lion")
lion.makeNoise()
lion.eat()
lion.move()

cat = Cat("Cat")
cat.makeNoise()
cat.eat()
cat.move()