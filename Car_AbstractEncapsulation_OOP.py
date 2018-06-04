''' 1. Hatchback, Sedan, SUV should be type of cars that are being provided for rent

2. Cost per day:

Hatchback - $30

Sedan - $50

SUV - $100

3. Give a prompt to the customer asking him the type of car and the number of days he would like to borrow and provide the fare details to the user. '''


class Car:
    # Initialise variables

    def __init__(self, availablecars):

        self.availablecars = availablecars

    # Function to display available cars for rent

    def rentingCarsAvailability(self):

        print("Display available cars")

        for key in sorted(self.availablecars):
            print(key)

    # Function to find total cost of rented car

    def carRentDetails(self):

        print("Enter the car you want to rent")

        self.requestedcar = input()

        print("Enter number of days for rent")

        self.numberofdays = int(input())

        if self.requestedcar in self.availablecars:

            print("Total rent cost of", self.requestedcar, "for", self.numberofdays, "is $",
                  self.availablecars[self.requestedcar] * self.numberofdays)

        else:

            print("Incorrect car entered")


# creating an object, given input values

car = Car({"Hatchback": 30, "Sedan": 50, "SUV": 100})

car.rentingCarsAvailability()

car.carRentDetails()