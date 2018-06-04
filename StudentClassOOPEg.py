# create a class
class Student:
    # creating property or data for the class Student
    # there are two parameters name and cgpa to be passed, it's a local variable
    def __init__(self, name, gpa):
        # left side self.name is object variable (or) instance variable for the class Student
        # right side name is a local variable, doesn't belong to class Student
        self.name = name
        self.gpa = gpa

    # creating behaviour or function for the class Student
    # self keyword determine the function getGpa belong to which object
    def getGpa(self):
        return self.gpa

    # creating behaviour or function setGpa, which gets input gpa from user and assign to instance variable
    def setGpa(self, gpa):
        self.gpa = gpa

    # creating behaviour or function getName for the class Student
    def getName(self):
        return self.name

    # creating behaviour or function setName, which gets input name from user and assign to instance variable
    def setName(self, name):
        self.name = name

# creating object for the class Students
# it will call def _init_(self,name,gpa) in the class Student
john = Student("John", 3.7)

# calling getGpa() function with in the class Student
print(john.getGpa())

john.setGpa(4.0)
# calling getGpa() after changing the gpa
print(john.getGpa())

print(john.getName())

john.setName("Peter")
# calling getName() after changing the name
print(john.getName())
