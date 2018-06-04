# overriding and Super() method

# Base class
class Employee:
    def noOfWorkingHours(self):
        self.workinghours = 45

    def displayWorkingHours(self):
        print("display working hours", self.workinghours)


# Derived class
class Trainee(Employee):
    # Derived class overrides the same method of base class
    def noOfWorkingHours(self):
        self.workinghours = 44

    # Using super() method to set back to base class method
    def resetWorkingHours(self):
        # syntax is super().base class method name
        super().noOfWorkingHours()


# Instantiate trainee object
trainee = Trainee()
# it gets override method value of derived class
trainee.noOfWorkingHours()
# it displays override method value of derived class
trainee.displayWorkingHours()
# reset to base class methos value
trainee.resetWorkingHours()
# it displays value of base class
trainee.displayWorkingHours()